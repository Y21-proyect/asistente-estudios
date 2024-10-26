import random # conseguir numero al azar en un rango
import os # limpiar consola
import pyttsx3 # lectura en voz alta de frases
import time

eleccion=True
valor=''
valorA=''
valor1=''
valor2=''
valor3=''
frase=''

def clear_console(): #FUNCION LIMPIAR CONSOLA
    if os.name == 'nt': # selector de sistema operativo para borrar el texto de la consola
        os.system('cls')     # Comando para Windows
        
    else:
        os.system('clear')   # Comando para Unix/Linux/Mac

    return()

def sandra():
    preguntas=''
    preguntas=''
    letra=''
    frase=''


    engine = pyttsx3.init()
    engine.setProperty('rate',130)
    voices = engine.getProperty('voices')
    
    with open('preguntas.txt', 'r', encoding='utf-8') as bus:
        preguntas = bus.readlines()

    random.shuffle(preguntas) # desordenar líneas de preguntas

    for pregunta in preguntas: # leer liena a linea
        for letra in pregunta: # leer letra a letra
            frase=frase+letra
            if letra== '?':
                print (frase,'\n')
                engine.say(frase)
                engine.runAndWait()
                input()
                frase=''
            if letra =='\n':
                print (frase)
                engine.say(frase)
                engine.runAndWait()
                frase=''
                input()

def pregunton():
    preguntas=''
    preguntas=''
    letra=''
    frase=''

    
    with open('preguntas.txt', 'r', encoding='utf-8') as bus:
        preguntas = bus.readlines()

    random.shuffle(preguntas) # desordenar líneas de preguntas

    for pregunta in preguntas: # leer liena a linea
        for letra in pregunta: # leer letra a letra
            frase=frase+letra
            if letra== '?':
                print (frase,'\n')
                input()
                frase=''
            if letra =='\n':
                print (frase)
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
n=   '                    (Yogalidof 21)\n\n\n'

o=(a,b,c,d,e,f,g,h,i,j,k,l,ll,m,n)

for p in o:
    print(p)
    time.sleep(0.21)

time.sleep(0.7)

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
print ('    O mi página de programas gratuitos de codigo abierto en https://github.com/y21-proyect 
print ('    No hace falta que des un like, no vivo de esto. Un saludo \n\n    Doc \n\n\n    Pulsa culaquier tecla para continuar...')
input('')


clear_console()


while eleccion==True:   ##### MENU DE SELECCION
    print('\n\n    ### INDICE ###\n')
    print('    0 - Añadir preguntas y respuestas manualmente')
    print('    1 - Iniciar preguntas y respuestas modo lectura')
    print('    3 - Iniciar preguntas y respuestas modo a audio con Sandra')
    print('    5 - Activar modo audio con Sandra')
    print('    7 - Desactivar modo audio con Sandra')
    print('    -----------------------------')
    valorA= input ('    Eleccion: ')

    clear_console()

    if valorA==5:
        valor=''
        print ('    Para activar el modo audio y que te haga preguntas el ordenador, hay que instalar')
        print ('    antes unos programas de Python, necesitas tener conexiona internet\n\n')
        print ('    El programa bajará programas gratuitos que hay en internet y que pertenecen a un lenguaje')
        print ('    de programación mundialmente conocido llamado python. Es gratuito y muy utilizado en el día a día.\n')
        print ('    Si quieres que el programa añada cambios al ordenador pulsa 1 y luego ENTER')
        print ('    Si no quieres que el programa añada cambios al ordenador pulsa ENTER.')

        valor= input ('')

        if valor=='1':
            os.system('pip install pyttsx3')
            print ('Programas para audio instalados. Pulsa ENTER para continuar...')
            input('')
            valor=''

    if valor=='7':
            print('pulsa y i luego ENTER cuando deje de aparecer texto en pantalla\n\n')
            os.system('pip uninstall pyttsx3')
            valor=''
            input('')
     
    while valorA=='0': # PARTE DE AÑADIR PREGUNTAS Y RESPUESTAS
        valor1=''
        valor2=''
    
        valor1= input('Pregunta: ')
        valor2=input('Respuesta: ')

        print('\n\n', valor1, '  ', valor2)
        valor3= input ('¿quieres guardar esta pregunta y su respuesta en la memoria?. \nPulsa la tecla ENTER para sí, n para no, y s para guardar y volver al menu principal')
        
        if valor3=='' or valor3=='s':
            valor1='\n'+valor1+valor2
            if valor3=='s':
                valor=''
            with open('preguntas.txt', 'a', encoding='utf-8') as preguntas:
                preguntas.write(valor1)


    if valorA=='1':
        pregunton()
        
      
    if valorA=='3': # PARTE DE PREGUNTAS Y RESPUESTAS
        sandra()



