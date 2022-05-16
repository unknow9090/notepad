#this is sample space to learn to test
name = "project"
number = 1
string = "text"

print (name.title())
print (name.upper())
print (name.lower())
print (name.upper() + " " + str(number) + string )

cars = ['ducati' , 'bocati' , 'bnw' , 'swist' , 'desgier' , 'telsa']

print (cars[0])

print (cars[-1])
cars.append('text' )
cars.append( 'funk' )
cars.remove('ducati')

for model in cars:
    print ("this is text after result " + model)
    print ("this is waste not working list")

#cars.short()
print (cars)
len(cars)

for na in range(1,20):
    print (na)
    print ("this is number of output" + str(na) )
