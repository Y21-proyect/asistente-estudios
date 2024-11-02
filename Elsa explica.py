from PyPDF2 import PdfReader # pip install pypdf2
import pyttsx3 # librería lectura en voz alta
import random # conseguir numero al azar en un rango
import os # limpiar consola
import time


llave= True
llave2=True
llave3=True
pdf= ''
blanco=0
franja=0
franja1=0
elsa=''
validacion=''
pagina=''
pagina_aleatoria=0
contenido_pagina_aleatoria=[]
numero_frases=0
frase_aleatoria=0
puntero=0
linea=''
lineas=[]
frase_partida=''
letra=0
letras=0
mitad_letras=0.1
mitad_letras1=0
numero_letras=0
avanzar=''

def clear_console(): #FUNCION LIMPIAR CONSOLA
    if os.name == 'nt': # selector de sistema operativo para borrar el texto de la consola
        os.system('cls')     # Comando para Windows
        
    else:
        os.system('clear')   # Comando para Unix/Linux/Mac

    return()

def codg70(num,let,act):
      
      abc='a,b,c,d,e,f,g,h,i,j,k,l,ll,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
      ABC='A,B,C,D,E,F,G,H,I,J,K,L,LL,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
      NUM='0,1,2,3,4,5,6,7,8,9'
      SIMB= '¡,!,(,),[,],¬'

      cod=abc+','+ABC+','+NUM+','+SIMB
      cod70=cod.split(',')

      n=''
      s=0

      
      #codificado a  base 70

      if act==1:
            for n in cod70:
                  if s==num:
                        return(n)
                  s+=1

      if act==2:
            for n in cod70:
                  if n==let:
                        return(s)
                  s+=1


def db70ab10(letrs):
      num=0
      l=0
      n=''
      m=''
      o=0
      p=0
      q=0
      llave=0

      for n in letrs:  # proceso se hace escalonado de abajo hacia arriba, la llave 0
                   # multiplica el cociente por 5, la llave 1 le suma el ultimo cociente
                   # la llave 2 suma cocientes anteriores y multiplica por 70        

            l=int(codg70(num,n,2)) # cambio de codigo base 70 a base 10
            
            if llave==2:
                  p=l+(p*70) # multiplica por 70 operacion y suma resto hasta final de interación

            if llave==1: # suma el primer resto al proceso de la llave 0 durante la segunda iteracion
                  p= l+p
                  llave=2

            if llave==0: # multiplicar ultimo cociente por 70
                         # en la primera iteración
                  p=l*70
                  llave=1

              
      n=str(p)  

      return(n)            
            

def db10ab5(num):
      cif=int(num)
      llave=True
      n=''
      m=''
      o=''
      p=0
      
      while llave==True:
            p=cif%5
            cif=cif//5
            m=str(p)+m
            if cif<5:
                  m=str(cif)+m
                  llave=False

      return(m)



def db70ab5(num):
      
      num=db70ab10(num)
      return(db10ab5(num))
      

def animacion():   

      p=0
      q=0
      u=12
      s=''
      r=[]
      
      dib=('ak]7!u!2U','azjyyXii','afmU1J4i','bcQEEii','bcQnAPD','c9yO3W','c9yO3W','c9yO3W','akLKfE]ayQRb','akLKfE]dDm0S','akLKfE[]AuGN','akLKfE]al[aX','dZZp(CSNajN7')

      while p<13:
            if p==13:
                  break
            clear_console()
            r.append(p) # crea la figura que se crea en cada iteración
                        # dentro de la lista r
            q=12-p
            p=p+1

            print('\n\n\n')

            while q>0:
                  print('')
                  q=q-1
                  
            for s in r:
                  s=db70ab5(dib[s])
                  s=s.replace('4','').replace('3','y').replace('0',' ')
                  print('              '+s)


            time.sleep(0.000000007)

      time.sleep(0.7)
      
      print('\n\n               (Yogalidof 21 Proyect)')

      time.sleep(1)

      clear_console()

animacion()

print ('\n\n    Este programa es parte de un trabajo altruista y tambien de retos que me propongo')
print ('    La parte altruista és que facilita la vida a otras personas.')
print ('    Lograr retos que te propones és bueno para la salud, mantiene tu autoestima fuerte.')
print ('    Por ambas partes salgo beneficiado. No se si te suena esa frasecilla "ser inteligentemente egoísta"')
print ('    o el refrán "ayudar a terceros és ayudarse a uno mismo"\n\n')
print ('    Es un programa tipo codigo abierto, puedes ver el codigo de programación y cambiarlo con un')
print ('    programa para hacer programas, tipo IDLE). Es una forma de dar transparencia y que no está infectado\n\n')
print ('    Si te gusta este programa y quieres saber más cosas cuirosas puedes visitar mi canal \n    de youtube https://www.youtube.com/@yogalidof.21 ')
print ('    También visitar mi pagina y leer algunos libros gratis en \n    https://www.calameo.com/accounts/1582946  \n\n')
print ('    O mi página de programas gratuitos de codigo abierto en https://github.com/y21-proyect') 
print ('    No hace falta que des un like, no vivo de esto. Un saludo \n\n    Doc \n\n\n    Pulsa ENTER para continuar...')
input('')


os.system('cls')

print ('\n\n    Para que funcione este programa tiene que estar la misma carpeta donde')
print ('    está el pdf que quieres usar. El programa és muy sencillo y te irá guiando')
print ('    Pulsa ENTER para continuar')
input ('')

os.system('cls')

engine = pyttsx3.init() # configuración herramienta lectura
engine.setProperty('rate',130)
voices = engine.getProperty('voices')


while llave==True: #informacion sobre las paginas a estudiar

    z=os.system('dir')
    print ('--------------------------------------------------------------------------')
    print ('\n\n    En el listado de arriba aparecen los archivos pdf que tienes.')
    print ('    Son todos los que acaban en .pdf')
    print ('    A la izquierda te pone la fecha de creación, le sigue la hora en que se')
    print ('    cambió por última vez, la cantidad de memoria que ocupa y finalmente el nombre')
    print ('    No pongas el .pdf del final\n\n')

    pdf= input('    ¿cómo se llama el pdf? -- ')
    blanco= input('    ¿cuántas páginas hay sin numerar desde la portada hasta la numero 1?: ')
    franja= input('¿    cual és el número de la página de inicio del temario que quieres estudiar?  ')
    franja1= input('¿    cual és el número de la página final del temario que quieres estudiar?:  ')
    blanco=int(blanco)
    franja=int(franja)
    franja1=int(franja1)
    pdf=pdf+'.pdf'

    os.system('cls')
    
    print('    El pdf se llama', pdf)
    print('    Tiene ',blanco,' paginas sin numerar desde la portada hasta la página número 1')
    print('    El temario que quieres estudiar se inicia en la página ', franja, ' y finaliza en la página ', franja)
    validacion = input('    Si lo son correctos estos datos pulsa la tecla enter, si no pulsa \n    el botón 1 y luego pulsa enter\n\n ')

    if validacion=='':
        llave= False
        elsa= input('    ¿Quieres conocer a Elsa?, Pulsa 7 y ENTER. Si no la quieres conocer pulsa ENTER...   ')
        if elsa=='7':
            engine.say('Hola, soy Elsa. Encantada. Seré tu ayudante para estudiar. Te deseo mucha suerte en las evaluaciones. Besos.')

        os.system('cls')

    os.system('cls')


franja=franja+blanco   # sumar paginas en blanco iniciales a la pagina inicial seleccionada de preguntas
franja1=franja1+blanco    # sumar paginas en blanco iniciales a la pagina final seleccionada de preguntas

reader=PdfReader(pdf) # cargar en memoria pdf a leer


while llave2 == True:
     if llave3==True: # la llave se desactiva cuando se ha leído la página aleatoriamente
                      # y se tiene el número de líneas

         numero_frases=0
         puntero=0

         pagina_aleatoria= random.randint(franja,franja1) # obtener numero de pagina aleatorio
                 
         contenido_pagina_aleatoria = reader.pages[pagina_aleatoria] # obtener pagina aleatoria de pdf
         pagina=contenido_pagina_aleatoria.extract_text() # extaer contenido de pagina aleatoria
         pagina=pagina.replace('\n','').replace('.','.¬') #sacar saltos de linea y marcar el . final
         lineas=pagina.split('¬') # partir frase desde macas de puntos finales
 
         for linea in lineas: #contar las líneas de la página y desactivar llave2
                 numero_frases+=1
                 llave3=False
        
     numero_letras=0 # cuando cierra la llave 2, esas variables se van renovando tras cada x lineas leídas
     letras=0
     mitad_letras=0
     resto_mitad_letras=0
     frase_partida=''
     puntero=0

     os.system('cls') # limpia pantalla

     frase_aleatoria= random.randint(0,numero_frases) # obtener numero de linea aleatorio

     print ('--------- ESTAS EN LA PAGINA ',pagina_aleatoria,' DEL LIBRO -------------------')
     print('--- Para avanzar a la siguiente frase de esta página pulsa ENTER ---------------')
     print('--- Para cambiar de página al azar pulsa 1 y luego ENTER -----------------------\n\n')
         
      
     for linea in lineas:
        if puntero== frase_aleatoria: # localiza la linea al azar en la pagina
             for letra in linea: # cuenta las letras totales de la linea para partirla por la mitad
                 numero_letras+= 1

                 mitad_letras=numero_letras/2 # valor de posición de la mitad de letras de la linea

                 resto_mitad_letras=numero_letras%2 # operacion para comprovar se el valor es impar

                 if resto_mitad_letras!=0: # si el valor es impar suma 1 para hacerlo par
                     mitad_letras=(numero_letras+1)/2
                     mitad_letras1= int(mitad_letras)

             for letra in linea: # añade letras a mitad_letras hasta llegar a la mitad o final de la frase
                
                 frase_partida=frase_partida+letra 
                 letras+=1
                 
                 if letras==mitad_letras1: # primer valor que imprime de la linea, el segundo encima para finalizar bucle
                     print('---> ',frase_partida)
                     engine.say(frase_partida)
                     engine.runAndWait()
                     frase_partida=''
                     input('')
                     
                 if letras==numero_letras:
                     print('---> ',frase_partida)
                     engine.say(frase_partida)
                     engine.runAndWait()
                     numero_letras=0
                     input(' -----------------------------------------------------')
                     avanzar= input('Seleccion: ')
                     
                     if avanzar=='':
                         frase_partida=''
                         frase_aleatoria +=1

                    
        puntero+=1 # incrementa en 1 el valor del puntero que localiza la línea a imprimir

        if avanzar=='1': # abre la llave 2 y se elige otra página
            avanzar=''
            llave3=True
            os.system('cls')
            avanzar=''
            llave3=True
            os.system('cls')
