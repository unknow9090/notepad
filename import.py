

def main(name,surname,gender = '', exo = ''):

    pre ={}

    gender = input("enter")
    name = input("enter")
    surname = input("o")
    exo = input("exit")
    while True:
        pre['gender'] = gender
        pre['name'] = name
        pre['surname'] = surname

        if exo.lower() == 'exit':
            break
    return pre

last = main('name', 'surname',)
print(last)

main.name
