import random # conseguir numero al azar en un rango
import os # limpiar consola
import pyttsx3
import time

eleccion=True
valor=''
valorA=''
valor1=''
valor2=''
valor3=''
frase=''
cuestionario=''

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
     

def Elsa(listado):
    preguntas=''
    preguntas=''
    letra=''
    frase=''
    print('\n\n    PREGUNTAS DE: ',listado, '\n\n')

    engine = pyttsx3.init()
    engine.setProperty('rate',130)
    voices = engine.getProperty('voices')

    with open(listado, 'r', encoding='utf-8') as bus:
        preguntas = bus.readlines()

    random.shuffle(preguntas) # desordenar líneas de preguntas

    for pregunta in preguntas: # leer liena a linea
        for letra in pregunta: # leer letra a letra
            frase=frase+letra
            if letra== '?':
                print ('    ',frase,'\n')
                engine.say(frase)
                engine.runAndWait()
                frase=''
                input()

            if letra =='\n':
                print ('    ',frase,'\n')
                engine.say(frase)
                engine.runAndWait()
                frase=''
                input()

def pregunton(listado):
    preguntas=''
    preguntas=''
    letra=''
    frase=''
    print('\n\n    PREGUNTAS DE: ',listado, '\n\n')


    
    with open(listado, 'r', encoding='utf-8') as bus:
        preguntas = bus.readlines()

    random.shuffle(preguntas) # desordenar líneas de preguntas

    for pregunta in preguntas: # leer linea a linea
        for letra in pregunta: # leer letra a letra
            frase=frase+letra
            if letra== '?':
                print ('    ',frase,'\n')
                input()
                frase=''
            if letra =='\n':
                print ('    ',frase,'\n')
                frase=''
                input()

    return()


animacion()

clear_console()

print ('\n\n    Este programa es parte de un trabajo altruista y tambien de retos que me propongo')
print ('    La parte altruista és que facilita la vida a otras personas.')
print ('    Lograr retos que te propones és bueno para la salud, mantiene tu autoestima fuerte.')
print ('    Por ambas partes salgo beneficiado. No se si te suena esa frasecilla "ser inteligentemente egoísta"')
print ('    o el refrán "ayudar a terceros és ayudarse a uno mismo"\n\n')
print ('    Es un programa tipo codigo abierto, puedes ver el codigo de programación y cambiarlo con un')
print ('    programa para hacer programas, tipo IDLE). Es una forma de dar transparencia y que no está infectado\n\n')
print ('    Si te gusta este programa y quieres saber más cosas cuirosas puedes visitar esta web y leer')
print ('    algunos libros gratis en \n    https://www.calameo.com/accounts/1582946  \n\n')
print ('    O mi página de programas gratuitos de codigo abierto en https://github.com/y21-proyect') 
print ('    No hace falta que des un like, no vivo de esto. Un saludo \n\n    Doc \n\n\n    Pulsa ENTER para continuar...')
input('')


clear_console()


while eleccion==True:   ##### MENU DE SELECCION
    print('\n\n    ### INDICE ###\n')
    print('    0 - Elegir cuestionario')
    print('    1 - Añadir preguntas y respuestas manualmente')
    print('    2 - Añadir preguntas y respuestas de otra persona')
    print('    3 - Iniciar preguntas y respuestas modo lectura')
    print('    5 - Iniciar preguntas y respuestas modo audio con Elsa')
    print('    7 - Presentacion de Elsa')
    print('    -----------------------------')
    valorA= input ('    Eleccion: ')

    clear_console()

    if valorA=='0':  # PARTE AÑADIR CUESTIONARIO PARA PREGUNTAS
        z=os.system('dir')
        print ('--------------------------------------------------------------------------')
        print ('\n\n    En el listado de arriba aparecen los cuestionarios que tienes. \n    Son todos los que acaban en .txt \n    A la izquierda te pone la fecha de creación, le sigue la hora en que se\n    cambió por última vez, la cantidad de memoria que ocupa y finalmente el nombre\n')
        print ('    Indica solo el nombre del cuestionario a continuación.\n    Si no existe no te preocupes, escribe el nombre y el ordenador hará\n    automáticamente uno nuevo con el nombre que le esribas.\n    No pongas el .txt del final')
        cuestionario= input('\n    ¿Nombre del cuestionario?.... ')
        cuestionario=cuestionario+'.txt'
        print ('    Has elegido el cuestionario', cuestionario)
        input ('    Pulsa ENTER para volver a menu de inicio') 
        clear_console()

    while valorA=='1': # PARTE DE AÑADIR PREGUNTAS Y RESPUESTAS
        valor1=''
        valor2=''
    
        valor1= input('Pregunta: ')
        valor2=input('Respuesta: ')

        print('\n\n', valor1, '  ', valor2)
        valor3= input ('¿quieres guardar esta pregunta y su respuesta en la memoria?. \nPulsa la tecla ENTER para sí, n para no, y s para guardar y volver al menu principal')
        
        if valor3=='' or valor3=='s':
            valor1='\n'+valor1+valor2
            if valor3=='s':
                valor3=''
            with open(cuestionario, 'a', encoding='utf-8') as preguntas:
                preguntas.write(valor1)


    while valorA=='2': # PARTE AÑADIR PREGUNTAS DE OTRA PERSONA
        z=os.system('dir')
        print ('--------------------------------------------------------------------------')
        print ('\n\n    En el listado de arriba aparecen los cuestionarios que tienes. \n')
        print ('    Son todos los que acaban en .txt \n    A la izquierda te pone la fecha de creación')
        print ('    le sigue la hora en que se cambió por última vez, la cantidad de memoria que ocupa')
        print ('    y finalmente el nombre\n')
        print ('    Indica el nombre del cuestionario sin el .txt, o, da a ENTER pasa salir sin cambios')

        valor1= input('\n   ¿Nombre del cuestionario que quieres ampliar?.... ')
        valor1=valor1+'.txt'
        valor2= input('   ¿Nombre del cuestionario que quieres añadir al que amplias?.... ')
        valor2=valor2+'.txt'

        if valor1=='.txt':
            valor1=''
            valorA=''

 
        if valor1!='' and valor2!='':
                    print ('    Quieres ampliar el cuestionario: ', valor1, ' con el cuestionario ',valor2)
                    valor3= input ('    ¿Son correctos estos datos?. Pulsa ENTER para sí, n y luego ENTER para no...')
                    clear_console()

                    if valor3=='':
                        print('\n\n')
                        with open(valor2, 'r', encoding='utf-8') as bus:
                            preguntas = bus.readlines()
                            print('-----> Añadiendo preguntas y respuestas')
                            with open(valor1, 'a', encoding='utf-8') as bus:
                                for linea in preguntas:
                                    bus.write(linea)
                                    print(linea)
                        valorA=''
                        print('\n\n    Preguntas y respuestas de ',valor2, 'añadidas a ',valor1, '. Pulsa ENTER para salir')
                        input('')
                    else:
                        valorA=''

        clear_console

    
    while valorA=='3': # PARTE DE PREGUNTAS Y RESPUESTAS VISUAL
        pregunton(cuestionario)
        clear_console()
        
      
    while valorA=='5': # PARTE DE PREGUNTAS Y RESPUESTAS AUDIO
        Elsa(cuestionario)
        clear_console()
        

    if valorA=='7':
        engine = pyttsx3.init()
        engine.setProperty('rate',130)
        voices = engine.getProperty('voices')
        engine.say('Muy buenas, mi nombre és Elsa. Voy a ser tu asistencia de audio en las preguntas. Te deseo suerte en los estudios y doy animo para lograr tu objetivo. Mucha suerte, besos.')
        engine.runAndWait()

