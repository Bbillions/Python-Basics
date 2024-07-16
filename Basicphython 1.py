# python casting - this is the process of changing the type of your variable e.g from float to string or int
# x =float(4)
# print(x)

# # coverting float into integer
# X = int(4.5)
# print(X)

# # python input
# B = input('Enter yor name: ')
# print("My name is " +B)

# N = input('How old are you?: ')
# print("I'm " +N +" years old")

# # converting naira to dollar and dollar to naira
# dollar = input('Enter amount in dollar: ')
# print(int(dollar)*1540)

# Naira = input('Enter amount in Naira: ')
# print(int(Naira)/1540)


# # list - a collection and changeable
# # tuple - 
# # set
# # dictionary

# # LIST - it is also an array and squared bracket is used for it []
Foods = ['rice','beans','yam','garri']
print(type(Foods))
print(Foods[-1])

# changing things in your list
Foods[1] = 'Moi-moi'
print(Foods)
print(len(Foods))

# adding to the list - to the end of the list
Foods.append('plantain')
print(Foods)

# insert helps us to put it in the actual position that we want it
Foods.insert(2,"poundedyam")
print(Foods)

# remove
Foods.remove("poundedyam")
print(Foods)

# pop is also for removing, you'll just input the position..this helped us to remove rice
Foods.pop(0)
print(Foods)

# to clear everything out
Foods.clear()
print(Foods)

# Tuple - a collection which is ordered and unchangeable
Whot = ('square','star','rectangle','circle')
print(type(Whot))
print(Whot[1])

# the only thing you can do to atuple is printing it out and checking the length

# SET - its unordered and unindexed and are written with curly brackets
Fruits = {'orange','apple','pineapple','watermelon'}
print(Fruits)
print(type(Fruits))

# to add to the set and the add function is used because its unordered- YOU CAN ONLY ADD ONE
Fruits.add('banana')
print(Fruits)

# update a set - HELPS TO ADD MORE THAN ONE
Fruits.update(['cherry','mango','Quava'])
print(Fruits)

# len
print(len(Fruits))

# remove
Fruits.remove('Quava')
print(Fruits)
print(len(Fruits))


# discard - even when you are removing something thats not in the set, its not going to throw error unlike remove
# it performs the same function as remove.

# pop - because we are not sure of position, wed just run pop like that and may remove anything
Fruits.pop()
print(Fruits)

# clear
Fruits.clear()
print(Fruits)



