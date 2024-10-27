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
    time.sleep(0.07)

time.sleep(1)

os.system('cls')

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
print ('    You don``t need to give a like, I don`t live from this. Best regards \n\n    Doc \n\n\n    Press ENTER to continue...')
input('')


os.system('cls')


print ('    This little wizard is for installing libraries that python needs to work')
print ('    You must be connected to the internet. The program will download free programs that are available')
print ('    on the internet and that belong to a world-famous programming language called python')
print ('    which is free and widely used on a day-to-day basis.\n\n\n ')

input ('')


while valor=='0':
       print('    ###### MAIN #####\n ')
       print('    1- Install Programs Needed for Elsa Asks')
       print('    3- Installing Programs Needed for Elsa Explains')
       print('    5- Exit')
       print('    ---------------------------------------------------------')
       valor2= input('    Press the number key, then ENTER:  ')
       
       if valor2=='1':
              os.system('pip install pyttsx3')
              input ('presiona ENTER para finalizar')
              
       if valor2=='3':
            os.system('pip install pypdf2')
            os.system('pip install pyttsx3') 
            input ('Press the number key ENTER to exit')

       if valor2=='5':
              valor='1'  
