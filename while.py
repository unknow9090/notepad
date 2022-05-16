#put in there is an python error not reading details while loop input the text in list not print they saving only
#single data when we list print they showing entered values not key values
def name():
    details = True
    store = {}

    while details:
        print("enter your details as show in addhar card")
        print("if you want to quit just type exit")

        name1 = input("name in the details sur name \t")
        name2 = input("enter your  name \t")
        name3 = input("enter your father name \t")
        name4 = input("enter your mother name \t")
        name5 = 1
        name6 = 2

        store['surname'] = name1
        store['name'] = name2
        store['fathername'] = name3
        store['mothername'] = name4
        exi =  input( "if you want  to continous press any letter yes/no" + '' + "____")    
        if exi  == 'no':
            details = False
        print(list(store))
        print(len(store))
        print(type(store))

        for g in store.values():
            print(g)

        for x , s in store.items():
            print( str(x) + str(s))
            
        
name()


def name2(where,what):
    w = (where + "  " +  what)
    print(w)
    return w.capitalize()   
sun = name2('this' , 'that')
print(sun)