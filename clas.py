import math
import json
class Wonder():

    def __init__(self,name,age,gender,qualification):
        self.name = name
        self.age = age
        self.gender = gender
        self.qualification = qualification
        self.nask = 34
    
    def person(self):
        print(self.name + self.age)

    def engine(self):
        print("this is the text we wrote egine start")
        w = input()
        if w.lower() == 'quit':
            print('exit the program')
        
    

great = Wonder('name','23','male','fail')

great.person()


print(math.pi)
print(math.tan(9))

#with open('/home/parrot/ip' , 'a') as fi:
 #   fi.write('   this is we made too write')
  #  fi.write('what was going')
try:
   #with open('/home/parrot/number.json') as vi:
        e = json.load(vi)
        
except FileNotFoundError:
    print('your file is not found file path is error')
else:
    print(vi)
try:
    print(5/0)
except ZeroDivisionError :
    print('we cant print are divide with zeros')

#filename =['ip' ,'text.save.1']
##   for g in a :
      #  print(g)
pass


name = input('enter your name')

filename = '/home/parrot/number.json'
with open(filename , 'a') as q:
    json.dump('/home/parrot/number.json', q)