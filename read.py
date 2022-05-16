import json
import unittest



name =  input('enter your name')

with open('/home/parrot/number.json', 'a') as w :
    json.dump(name, w)

try:
    with open('/home/parrot/number.json', ) as p :
     fu = json.load(p)
     print(fu)
except json.decoder.JSONDecodeError:
    print("this is waste")


def get_information(first,last):
    
    fullname = first +  ' '+last
    return fullname
    def whileloop():
            #while loop get the information
    
       while True:
               print('if you want to quit type exit')
               first = input('enter your first name  ')
               last = input('enter your middle name  ')
       
               if first.lower() =='q':
                break
               if last.lower() == 'q':
                 break



try :
 nameq = get_information(first , last)
except  NameError:
    print('wrong code')

get_information('sd','sds')
unittest.main()