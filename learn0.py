import typing_extensions

def list1():
    name = ["wjay","what","where we are","where"]
    print(name)
    for name2 in name:
        print(name2 + "what was the word")

        print(type(name))

        if name2.lower() == 'where':
            name3 = input("enter s number")
            print(name3.capitalize())
            break 
list1()
def list2():
    dem = ['name','name2','name3','name4','name5']
    dem2 = ['name1','name2','name3','name4','name5']
    

    for dem0 in dem:
        if dem in dem2:
            print("this is smaple space of + dem0")
        else:
            print("you are out of the if statment")
            break

def name_plate():
   age = input("enter your AGE of the current year")
   age = int(age)
   if age > 14 :
       print("you are the worst")
   elif age < 14:
        print("you not entered any thing ")
     
def dictonary():
    dic ={'color':'green','colour':'green' }
    print(dic['color'])
    print(dic['colour'])
    dic['wonder'] = "dark"
    dic['number'] = 5
    print(dic)
    for number_1 ,number_2 in dic.items():
        print(number_1 + ":" + str(number_2))


list2()
name_plate()
dictonary()