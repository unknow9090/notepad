name1 = "this is the text1"
name2 = "this is the text1 of variables"
name3 = "    this is the text3 of variables"
nam33 = 2222

#we created a there variabeles

#print(name1.upper() + "\t" + name2.title()+ +"\n" + "\t" + name3())

print(name1)
print(name2)
print(name3)

print(name1.title()+"\t "+name2.upper()+" \n"+name3.lower()+"\n "+name3+str(nam33))

var = (name1.title()+"\t "+name2.upper()+" \n"+name3.lower()+"\n "+name3+str(nam33))
var.strip
print(var)

var_number = 1
var_number2 = 2 
var_number3 = 3
var_number4 = 5
var_number4 = '6 this is strip'

#prin =  str( str(var_number + str(var_number2)+str(var_number3)+str(var_number4)))

#print(prin)

list_d = ["2",'this is', 'whta',"where am i","what tge fuxk"]

number_d = ['1','2','3','4']

print(list_d)
for var in list_d:
    print(var)

for number in number_d:
     print(number)
    
print(list_d[-1])
number_d.append("text")
number_d.insert(0,"what that is wrong")
del number_d[3]
number_d.remove('text')
print(number_d)
