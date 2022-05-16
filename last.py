def animal(cat =1,dog=2):
     where = str(cat) + str(dog)
     return where
fuck = animal('water','met')
print(fuck)

def waste_function(name,name3):
     full =  name + name3
     return full
fuck = waste_function('dad', 'mim')
print(fuck)

def cal(x):
     print('d')
     x = str(x)
     if int(x) % 2 ==  0 :
          print('it was even number')
     else :
          print('it was odd number')
cal(x=input())
def cal2(x=input()) : 
     if int(x) %2 ==0 : 
          print('it was even number')  
     else :('it was odd number')
cal2()

def worst(*num):
     for i in num:
          print(i)
     print(num)
worst('waste','worst','wonder','where')

def fun(fist = input(), last = input(), middle = input()):
     if middle:
          print(f'enter middle name{middle}')
     else:
          print('this is ok')
fun()
def person(first = input(), last = input(), middle = input()):
     na = {first : 'first',last : 'last',middle : 'middle'}
     return na
var = person()
print(var)