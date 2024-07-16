# 1.	Create variable of different data types(int, float, str) and peform a type 
# conversion between the data types and print the results.

x = 3
X = 'John'
W = 4.0 
t = True
O = 3j

print(type(x))
print(type(X))
print(type(W))
print(type(t))
print(type(O))

# casting
P = str(x)
print(P)
print(type(P))

# 2.	Perform arithmetic operations involving different types and demonstrate how casting can be used 
# to handle these operations. Example: Adding an integer and a float, concatenating an integer 
# with a string after casting.

R = int(x) + int(W)
print(R)

P = str(x)
Q = ('The drama between me and you took ' + (X) +  (P) + ' days')
print(Q)

# 3.	Create a list of integers and perform various operations such as adding, removing, and slicing elements
intlist = [1,2,3,4,5] 
print(intlist)

# to add to the end of the list
intlist.append(7)
print(intlist)

# to add to a specified location
intlist.insert(5,6)
print(intlist)

# to remove and item in the list using pop - you put in the index of the number you want it to POP
intlist.pop(6)
print(intlist)

# to remove using remove - you put in the actual number you want it to remove
intlist.remove(5)
print(intlist)

# slicing element

# print the last item to the back
print(intlist[-1])

# to print the first 3 items
print(intlist[0:3])

# 4.	Create a set of integers and demonstrate adding and removing elements.
Fruits = {'orange','Banana','Quava','Lemon'}
print(Fruits)

# to add more friuts
Fruits.add('Pineapple')
print(Fruits)

# to add more than one
Fruits.update(['Cucumber','Carrots'])
print(Fruits)

# removing items from fruits sets - remove, discard, pop
# remove will throw in error if it can't find the item you want to remove but discard will just let it slide
Fruits.remove('Quava')
print(Fruits)

# to discard
Fruits.discard('Carrots')
print(Fruits)

# to pop- since it does not have an order nor indexed, it will just remove anything
Fruits.pop()
print(Fruits)

# 5.	Create a dictionary and perform operations such as adding, updating, and deleting key-value pairs.
Dictt = {'Oyo':'Ibadan','Plateau':'Jos','FCT':'Abuja'}
print(Dictt)

# add to a dict
Dictt["Edo"] = "Benin"
print(Dictt)

# to update
Dictt = {'Oyo':'Ibadan','Plateau':'Jos','FCT':'Abuja'}
new_data = {'Benue':'Markurdi','Borno':'Maiduguri'}
Dictt.update(new_data)
print(Dictt)

# it removes the item you want it to remove
print(Dictt.pop('Oyo'))
print(Dictt)

# popitem = removes the last item
print(Dictt.popitem())
print(Dictt)

# 6.	Write a program that checks if a number is positive, negative, or zero.
Rate = int(input('Enter your value in here: '))
if Rate > 0:
    print('Gege, positive number')
elif Rate < 0:
    print('The number you entered is negative')
else:
    print('You entered zero oooo')

# OR

Rate = int(input('Enter your value in here: '))
if Rate > 0:
    print('Gege, positive number')
elif Rate == 0:
    print('You entered zero oooo')
else:
    print('The number you entered is negative')

# 7.	Write a program to check if a given number is even or odd.
Num = int(input('Put in your value: '))
if Num %2 == 0:
    print('Your number is even!')
elif Num %2 != 0:
    print('You have entered an odd number ')

# 8.	Write a program to check if a given character is a vowel or consonant.
CheckAlpha = str(input('Put in your alphabet here: '))
if (CheckAlpha == 'a' or CheckAlpha == 'e'or CheckAlpha =='i' or CheckAlpha == 'o' or CheckAlpha == 'u'):
    print('its a vowel sound')
else:
    ('My dear, its consonant')

# OR
vowel = str(input('Enter your alphabet'))
if vowel in  "aeiou":
    print('vowel')
else:
    print('Consonant')

# 9.	Write a program that simulates a simple login system.
#  Check if the entered username and password match the stored username and password.
username = str(input('Enter your username: '))
password = int(input('Enter your four digits password: '))
if username == 'BBillions' and password == 2024:
    print('You have the access')
# OR
username = str(input('Enter your username: '))
if username == 'BBillions':
    print('Welcome the billionaire, now put in your password')
password = int(input('Enter your four digits password: '))
if password == 2024:
    print('You have the access')

# 10.	Write a function that takes two numbers 
# and an operator (+, -, *, /) and returns the result of the operation.
def twonum(x,y,operator):
    if operator == '+':
     return x + y
    elif operator == '-':
     return x - y      
    elif operator == '*':
        return x*y
    elif operator == '/':
        return x/y
    else:
        return "invalid operator"
print(twonum(3,4,'+'))


# 11.	Write a function that takes a list of numbers and returns a new list with each number squared.
def SQR(num):
    Sqrnumber = []  
    for x in num:
        Sqrnumber.append(x**2)
    return Sqrnumber
num = [2,3,5]
print(SQR(num))

# 12.	Write a function that takes a number and returns "Even" if the number is even and "Odd" if the number is odd.
def numbercheck():
    Num = int(input('Put in your value: '))
    if Num %2 == 0:
        print('Your number is even!')
    else:
        print('You have entered an odd number ')
numbercheck()
# 13.	Write a program to create a function that takes two arguments, name and age, and print their value.
def Nameage(name,age):
    print(name + str(age))
Nameage('Alade ', 10)
    
# 14.	Find the largest item from the list X = [4,6,8,24,12,2]
X = [4,6,8,24,12,2]
maximum = max(X)
print(maximum)

# 15.	Write a program that prints all elements of a list using a  for loop.
def printing():
    printer = [1,2,3,4,5,6]
    for i in printer:
        print(i)
printing()

# 16.	Write a program that prints the numbers from 1 to 10 using a  for loop.
numten = range(1,11)
for i in numten:
    print(i)

# 17.	Write a program that prints each character of a string on a new line using a  for loop
string = 'Pineapple'
for i in string:
    print(i)
    
# 18.	Write a program that calculates the sum of a list of numbers using a  for loop.
def summing(num):
    Total = 0
    for x in num:
        Total += x 
    return Total
num = [1,2,3,4,5]
print(summing(num))

# or
num = [1,2,3,4,5]
Total = 0
for x in num:
        Total += x 
print(Total)

# 19.	Write a program that prints all even numbers from 1 to 20 using a for loop.
for i in range(2,21,2):
    print(i)

# 20.	Write a program that prints the square of each number from 1 to 10 using a for loop.
for i in range(1,11):
    print(i**2)

