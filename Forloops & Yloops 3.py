# learn about grading in the university system
# 0-39 = f9
# 40-44 = E8
# 45-49 = D7
# 50-54 = c6
# 55-59 = C5
# 60-64 = C4
# 65-69 = B3
# 70-74 = B2
# 75-100 = A1
# myinput = input('Enter your score: ')
# print(myinput)
# if myinput.isnumeric() == True:
#     newinput = int(myinput)

# if newinput < 0 and newinput > 100:
#     print('invalid score')
# else:
#     if newinput <=39:
#         print('F9')
#     elif newinput <=44:
#         print('E8')
#     elif newinput <=49:
#         print('D7')
#     elif newinput <=54:
#         print('C6')
#     elif newinput <=59:
#         print('C5')
#     elif newinput <=64:
#         print('C4')
#     elif newinput <=69:
#         print('B3')
#     elif newinput <=74:
#         print('B2')
#     elif newinput <=100:
#         print('A1')


# # forloops & whileloops
# # forlops - trying to write acess to each of them
# Foodie = ['Rice','Beans','Egg','Fish','Meat']
# for Food in Foodie:
#     print(Food + str(20))

# # WITH numbers
# Number = [1,2,3,4,5,6]
# for Num in Number:
#     print(Num * 3)

# # working with just a variable
# for x in 'Banana':
#     print(x)

# # WITH numbers - just to print one number
# Number = [1,2,3,4,5,6]
# for Num in Number:
#     if Num == 3:
#         print(Num)


# # WITH numbers - to break at a point and ignore the rest
# Number = [1,2,3,4,5,6]
# for Num in Number:
#      print(Num)
#      if Num == 3:
#          break
        

# 28/5/24
# to use continue
Fruits = ['Apple','Banana','Pineapple']
for Fru in Fruits:
     if Fru == 'Banana':
         continue
     print(Fru)


# Range - this will print from 0-5
for x in range(6):
     print(x)

# range with two values
for x in range(1,6):
     print(x)

# range between numbers and specifying the space between the numbers-starting point,range if numbers and no of space
for x in range(1,6,2):
     print(x)

# to print out two responses
for x in range(0,2):
     print('Welcome.....!!!!!!!!')

# to print out the even number in this set
list_number = [1,2,3,4,5]
for x in list_number:
     if x%2 ==0:
          print(x)

# to print out odd numbers
list_number = [1,2,3,4,5]
for x in list_number:
     if x%2 == 1:
          print(x)

        #   OR
list_number = [1,2,3,4,5]
for x in list_number:
     if x%2 != 0:
          print(x)


# WHILE LOOPS - starting point, condition and increment
I = 0
while I<6:
     print(I)
     I+=1

i=0
while i<=20:
     print(i)
     i+=2





