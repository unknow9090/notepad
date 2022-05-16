import threading     
from math import pi as p 
from Testing import __init__


def main(first_name , Last_name):

    full = (first_name + " "+ Last_name)

    
    return full.upper()

    print(full)

fuck = main('dictonary.py', 'dictonary.py')

print(fuck)
file_path =  '/home/parrot/Desktop/new'
with open(file_path) as inpu :
    w  = inpu.readlines()
    print(w)