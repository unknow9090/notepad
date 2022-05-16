
import time




def var(name, user_del = 'text'):
    print("hello")
    print (name + str(user_del))
var('python' , 1 )
var('python' , 1 )

def combine(user , user2):
    fullname = user + user2
    return fullname
combine('dtext' , 'wonder')


#myage = input()

#print('after ten year your age'+ str(int(myage) + 10))


print(2+2 == 2+2 and not 2 == 3 and 55 == 55)
print(2+2 == 6 or 5 == 8)
 
if not 2+2 == 4 and 4 != 5 and not 10 == 20:
    print('this is the text we wroght')
else :
    print('out') 


name = ''

while name != 'your name':

    print('your name')
    name = input()

    print(str(name))


while True:
    print('enter your name')
    name = input()
    if name != 'name':
        continue
    print('hello world ')
    passw = input('enter your pass')
    if passw == 'text':break

print('welcome back')

