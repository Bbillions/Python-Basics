# 21-05-24
# the difference between sets and dictionaries have the same bracket but they are different because dictionaries
# have key and values

new_student = {
    "name":"John",
    "age":20,
    "Gender":"male"
}
print(new_student)

# this is just to print one thing in the dictionary
x = new_student["Gender"]
print(x)

# add more to the dictionary
new_student["colour"] = "red"
print(new_student)

# to check the length
print(len(new_student))

# to remove - only the pop method works for dictionaries
print(new_student.pop("colour"))
print(new_student)
# popitem - this function removes the last item
print(new_student.popitem())
print(new_student)

# # conditional statements... if, else & elif
# A = 30
# B = 10
# if A>B:
#     print('A is greater than B')
# else:
#     print('A is less than B')

# # or
# A = 3
# B = 10
# if A>B:
#     print('A is greater than B')
# else:
#     print('A is less than B')

# # or
# A = 10
# B = 10
# if A>B:
#     print('A is greater than B')
# elif A==B:
#     print('A is equal to B')
# else:
#     print('A is less than B')

# # the one with input
# A = input('Enter A: ')
# B = input('Enter B: ')
# if A>B:
#     print('A is greater than B')
# elif A==B:
#     print('A is equal to B')
# else:
#     print('A is less than B')

# AND / OR CONDITION

# Score = 201
# Age = 18
# if Score > 200 and Age >= 18:
#     print("FANTASTIC!, You are eligible for Admission")
# elif Score == 200 and Age == 18:
#     print("You are on point!")
# else:
#     print("You are not eligible for Admission")

# Write a program to check if you are eligible for voting or not
# age = int(input("ENTER YOUR AGE: "))
# if age > 18:
#     print('You are eligible to vote!')
# elif age == 18:
#     print('You can now exercise your right as a Nigerian')
# else:
#     print('Go back home and pray for our country')

# University of ibadan requires student to score 50 in both English & Maths to be considered for Admission,oau 
#requires to score at least 50nin any of them, write a condition to check if a student is admissible to ui or not

Maths = int(input('Enter your score in Mathematics: '))
English = int(input('Enter your score in English: '))
if Maths > 50 and English >50:
    print('university of Ibadan welcomes you')
elif Maths == 50 and English == 50:
    print('God saved you to UI')
elif Maths >= 50 or English >=50 :
    print('OAU admits you, Welcome')
else:
    print('Stop playing on tiktok, face your life! ')






