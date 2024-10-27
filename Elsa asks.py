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
    print('\n\n    QUESTIONS FROM: ',listado, '\n\n')

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
    print('\n\n    QUESTIONS FROM: ',listado, '\n\n')


    
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

print ('\n\n    This program is part of an altruistic work and challenges that I propose to myself.')
print ('    The altruistic part is that it makes life easier for other people.')
print ('    Achieving challenges is good for your health, it keeps your self-esteem strong.')
print ('    it is beneficial on two sides. I don`t know that little "be intelligently selfish"')
print ('    or the saying "helping others is helping oneself"\n\n')
print ('    It`s an open source type program, you can see the programming code and change it with a')
print ('    program to make programs, type IDLE. It is a way of providing transparency and that it is not infected\n\n')
print ('    If you like this program and want to know more curious things you can visit my channel \n    de youtube https://www.youtube.com/@yogalidof.21 ')
print ('    Also visit my page and read some free books on \n    https://www.calameo.com/accounts/1582946  \n\n')
print ('    Or my free open source programs page en https://github.com/y21-proyect')
print ('    Some important, my webs are in spanhis lenguaje')
print ('    You don`t need to give a like, I don`t live from this. Best regards \n\n    Doc \n\n\n    Press ENTER to continue...')
input('')


clear_console()


while eleccion==True:   ##### MENU DE SELECCION
    print('\n\n    ### MAIN ###\n')
    print('    0 - Choose Quiz')
    print('    1 - Add questions and answers manually')
    print('    2 - Add one quiz to another one')
    print('    3 - Start Q&A in reading mode')
    print('    5 - Start Q&A audio mode with Elsa')
    print('    7 - Introducing Elsa')
    print('    -----------------------------')
    valorA= input ('    Selection: ')

    clear_console()

    if valorA=='0':
        z=os.system('dir')
        print ('--------------------------------------------------------------------------')
        print ('\n\n    The list above shows the quiz you have.')
        print ('    They are all those who end up in.txt. On the left it puts the date')
        print ('    of creation, followed by the time it was last changed, the amount')
        print ('    of memory that it occupies and finally the name\n')
        print ('    Type only the name of the quiz below. If it doesn`t exist, don`t')
        print ('    worry, type in the name and the computer will automatically make a new one')
        print ('    with the name you write it. Don`t put the .txt at the end')
        cuestionario= input('\n    ¿Quiz Name?.... ')
        cuestionario=cuestionario+'.txt'
        clear_console()

    while valorA=='2': # PARTE AÑADIR PREGUNTAS DE OTRA PERSONA
         os.system('dir')
         print ('--------------------------------------------------------------------------')
         print ('\n\n    The list above shows the quiz you have.')
         print ('    They are all those who end up in.txt. On the left it puts the date')
         print ('    of creation, followed by the time it was last changed, the amount')
         print ('    of memory that it occupies and finally the name\n')
         print ('    Type only the name of the quiz below, do not put the .txt at the end')
         print ('    or type ENTER to exit')

         valor1= input('\n   ¿Name of the quiz you want to expand?.... ')
         valor1=valor1+'.txt'
         valor2= input('   ¿Name of the quiz you want to add to the one you expand?.... ')
         valor2=valor2+'.txt'

         if valor1=='.txt':
            valor1=''
            valorA=''

         if valor1!='' and valor2!='':
             print ('    You want to expand te quiz ', valor1, ' with the quiz ',valor2)
             valor3= input ('    Are these data correct? Press ENTER for yes or n and then ENTER for not...')
             clear_console()

             if valor3=='':
                 print('\n\n')
                 with open(valor2, 'r', encoding='utf-8') as bus:
                     preguntas = bus.readlines()
                     print ('-----> Adding quizs:')
                     with open(valor1, 'a', encoding='utf-8') as bus:
                              for linea in preguntas:
                                   bus.write(linea)
                                   print(linea)
                 valorA=''
                 print('\n\n Quiz from ',valor2, 'added to ',valor1,'. Push ENTER to exit')
                 input('')

             else:
                valorA=''

         clear_console()
        


    while valorA=='1': # PARTE DE AÑADIR PREGUNTAS Y RESPUESTAS
        valor1=''
        valor2=''
    
        valor1= input('Question: ')
        valor2=input('Answer: ')

        print('\n\n', valor1, '  ', valor2)
        valor3= input ('Do you want to keep this question and its answer in memory? \nPress the ENTER key for yes, n and ENTER for no, and s and ENTER to save and return to the main menu')
        
        if valor3=='' or valor3=='s':
            valor1='\n'+valor1+valor2
            if valor3=='s':
                valor3=''
            with open(cuestionario, 'a', encoding='utf-8') as preguntas:
                preguntas.write(valor1)


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
        engine.say('Very good, my name is Elsa. I`m going to be your audio assistance in the quiz. I wish you good luck in your studies and I encourage you to achieve your goal. Good luck, kisses.')
        engine.runAndWait()


