import os
import time

valor='0'
valor2=''

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

time.sleep(1)

os.system('cls')

print ('\n\n    Este programa es parte de un trabajo altruista y tambien de retos que me propongo')
print ('    La parte altruista és que facilita la vida a otras personas.')
print ('    Lograr retos que te propones és bueno para la salud, mantiene tu autoestima fuerte.')
print ('    Por ambas partes salgo beneficiado. No se si te suena esa frasecilla "ser inteligentemente egoísta"')
print ('    o el refrán "ayudar a terceros és ayudarse a uno mismo"\n\n')
print ('    Es un programa tipo codigo abierto, puedes ver el codigo de programación y cambiarlo con un')
print ('    programa para hacer programas, tipo IDLE). Es una forma de dar transparencia y que no está infectado\n\n')
print ('    Si te gusta este programa y quieres saber más cosas cuirosas puedes visitar esta web y leer algunos libros')
print ('    gratis en \n    https://www.calameo.com/accounts/1582946  \n\n')
print ('    O mi página de programas gratuitos de codigo abierto en https://github.com/y21-proyect') 
print ('    No hace falta que des un like, no vivo de esto. Un saludo \n\n    Doc \n\n\n    Pulsa ENTER para continuar...')
input('')


os.system('cls')


print ('    Este pequeño asistente és para instalar bibliotecas que necesita python para funcionar')
print ('    Has de estar conectado/a a internet para que funcione. El programa bajará programas gratuitos que hay')
print ('    en internet y que pertenecen a un lenguaje de programación mundialmente conocido llamado python')
print ('    que és gratuito y muy utilizado en el día a día.\n\n\n ')

input ('')


while valor=='0':
       print('    ###### MENU #####\n ')
       print('    1- Instalar programas necesarios para Elsa pregunta')
       print('    3- Instalar programas necesarios para Elsa explica')
       print('    5- Salir')
       print('    ---------------------------------------------------------')
       valor2= input('    Pulsa la tecla del número y luego ENTER:  ')
       
       if valor2=='1':
              os.system('pip install pyttsx3')
              input ('presiona ENTER para finalizar')
              
       if valor2=='3':
            os.system('pip install pypdf2')
            os.system('pip install pyttsx3') 
            input ('presiona ENTER para finalizar')

       if valor2=='5':
              valor='1'  


