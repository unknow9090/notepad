import sys,copy
import math

def dictonary1() :
       dic1 = {'user_name' :{'location' : '1254.02445.2122' , 'wether':'negative','chargeing' : '25%','device':'mobile'}}
       c1 = {'user_name2' :{'location' : '1254.02445.2122' , 'wether':'negative','chargeing' : '25%','device':'mobile'}}
       c3 = {'user_name3' :{'location' : '1254.02445.2122' , 'wether':'negative','chargeing' : '25%','device':'mobile'}}
       c4 = {'user_name' :['vakue ','not vales' ,'number','2','sex','male','age','21']}

       list_user = [dic1 , c1,c3]
       zv = copy.deepcopy(c1)

       print   (list_user)

       for value1 , key1  in dic1.items():
              print(value1 )
              for key1 ,key2 in dic1.items():
                     print(key1  )
                     for key2  in dic1.items():
                            print(key2) 
       
       for var1, var2 in c4.items():
              print( "val is the car" + var1)
              for var3 in var2:
                     print("this is the world outer ruler" + "  " + var3)
       
       for var5,var6 in c1.items():
              print ("\n user name is \n" + var5)
              location = "this is your location " + var6['location'] +"\n"+  "your wether at that time \t" + var6['wether']
              chargeing = "this is your chargeing of the mobile\n" + var6['chargeing'] + "\t" +"your device login \n" + var6['device']

              print("this is the varabile of the texyt" + var5)

              print(location + chargeing)

   
   
                     
       dic1.update(c4 )
       print((dic1))
              

       type(dic1)
       print(type(dic1))
       dic1.update([('value','notvalid'),('gender' , 'male'),('age','15'),])
       print(dic1)
       
       print(list(dic1.items()))

       empty = []

       for wonder in range(10):
              insert1 = {'wonder' : 1 , 2:2 ,3:4}
              empty.append(insert1)
       for wonder in empty[3:]:
              print(wonder)

       print(math.pi)
       #if location in dic1 :
        #      print("gender is avalible")
       co = 1
       while True :
              if co < 5:
                     print(co)
                     co +=1
                     break

def Merage(dic1,c1):
       return(dic1.update(c1))

       print(Merage(dic1, c1))

 
dictonary1()