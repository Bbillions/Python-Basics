# Functions - its a block of code that only runs when its called.(function name & parameters )
def greetings():
    print('Welcome here!!!!!!')
greetings()# functions with parameter
def student(Fname):
    print(Fname + ' Adeleke')


student('Wura')
student('Tony')
student('Lolu')
student('Eve')

# defining functions for adddition
def add(a,b):
    print(a+b)
add(5,6)

# arbituary argument - when you dont know the number of arguments to pass and its represented with *
def my_kid(*kid):
    print('My youngest child is ' + kid[2])
my_kid('Wura','Ade','Sayo')

