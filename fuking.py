class Learn:

    def __init__(self,name,dog,bread,age,year):
        self.name = name
        self.dog = dog
        self.bread = bread
        self.age = age
        self.year = year

    def dog_name(self):
        self.name = input("enter your dogname")
        print("this is ok but we need to more to learn")
        print(self.name)

    def dog_age(self):
        self.age = input("enter age")
        self.age =str(self.age)

        if self.age != 10:
            s = input('if dog any suffers with infections \t')
            if s == 'yes':
                w  = input('what was happend')
                print(w)
            elif s == 'no':
                 print('ok we will dicuss it later')
    def collect(self) :
        print('your entred details of the dog') 

        print(f'name of the dog == > {self.name}' + ' dog age your entred '+ self.age )

    #class infection(Learn):
     #   def suck() :
      #      print('this is sucks text')
                    
f = Learn('name', 'dog', 'bread', 'age', 'year')

f.dog_name()
f.dog_age()
f.collect()
f.infection.suck()