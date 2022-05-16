

def dict1():
        interger = {1:'pavan', 2:'harsha', 3: 'noothana', 4:'uma' ,5: 'ramarao', 6:'kondama' ,7:'nandhi' }
        strings = {'name' : "harsa" , "name2" : "pavan", "name3" :"kiran kumar", "name4" : "sudheer"}
        dict_loop1 = {'family1':{'father':'krishna','mother':'kalavathi','son': 'kiran','son2':'sudheer','daughter':'kalavati'} ,
        'family2':{"father" : "shankar rao", "mother":"sridevi" ,"son":"harsha","daughter" :"noothna",'son2' : ''} }
        tuple1 = {1:("shankara rao",'sridevi','harsha','nootha'),2:('tatata','mama','ravi','kishore','srerisha','daughter2')}
        list1= {1.2:["shankara rao",'sridevi','harsha','nootha'],1.3 :['tatata','mama','ravi','kishore','srerisha','daughter2']}
        aadd = {'mumbai','pune','chennai','delhi','kolkata'}
        add2 ='city'
        add1 = dict.fromkeys(aadd,add2)

        print(type(add1))

        print(add1 )


        interger[8] = 'nandhi2'
        del interger[3]
        print(list(interger))
        dict_loop1.setdefault('wo','not')
    
        int2 = interger.get(1)
        print(int2)

        for i , x in interger.items() :
            print(int(i) )
            print("===>" + x)
        
        for z , v in dict_loop1.items():
            print(z +" == "+ "is family members")
            father_name =str(v['father'])
            mother_name = v['mother']
            son_name  = v['son']
            son_nmae2 = v['son2']
            daugther_name = v['daughter']
            print('FATHER NAME ==' + father_name)
            print("MOTHER NAME ==" + mother_name)
            print('son NAME ==' + son_name)
            print('DAUTHER NAME ==' + daugther_name)
        for c,b in list1.items() :
            print(c)
            for second in b:
                print(second)
        for d , k in tuple1:
            print(d + k)
             
 
        

        
dict1()