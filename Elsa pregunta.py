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


a='\n\n'
b=   '                 yyyy          yyyy   '
c=   '                  yyyy        yyyy    '
c=   '                   yyyy      yyyy     ' 
d=   '                    yyyy    yyyy      ' 
e=   '                     yyyy  yyyy       ' 
f=   '                      yyyyyyyy        ' 
g=   '                        yyyy          ' 
h =  '                        yyyy          ' 
i =  '                        yyyy          ' 
j =  '                        yyyy    222       1   ' 
k =  '                        yyyy   2   2    1 1   ' 
l=   '                        yyyy      2       1   ' 
ll=  '                        yyyy    2         1   '  
m=   '                        yyyy   22222    11111 \n\n '
n=   '                    (Yogalidof 21)'

o=(a,b,c,d,e,f,g,h,i,j,k,l,ll,m,n)

for p in o:
    print(p)
    time.sleep(0.07)

time.sleep(1)

clear_console()

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
