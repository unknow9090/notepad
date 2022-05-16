store_data = {}

get_detials = True

while get_detials:
    name = input("enter your name") 
    store_data1 = input("what is your aim")
    store_data[name] = store_data1 

    repeat = input("whould you like to contione yes/no")
    if repeat == 'no':
        get_detials = False
for store_data1, name in store_data.items():
    print(store_data1 , name)
print(store_data)

