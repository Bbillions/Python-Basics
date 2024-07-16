# Creating a class

class Myclass():
    x = 5
    y = 10
p1 = Myclass()
print(p1.x)
print(p1.y)

# Creating a function inside a class

class Person():
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age    
p2 = Person('uncle sam', 'male', 33)
p3 = Person('miss Gloria', 'female',27)
print(p2.name)
print(p3.age)

class Person():
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    def __str__(self) -> str:
       return f'my name is {self.name} my gender is {self.gender}'
p2 = Person('uncle sam', 'male', 33)
p3 = Person('miss Gloria', 'female',27)
print(p2)
print(p3)

# creating a class, dog

class Dog():
    def __init__(self,breed,size,color,gender,name,height,weight):
        self.breed = breed
        self.size = size
        self.color = color
        self.gender = gender
        self.name = name
        self.height = height
        self.weight = weight

    def run_speed(self):
        if self.breed.lower() == 'bulldog':
            return 'The dog speed is normal'
        elif self.breed.lower() == 'chihuahua':
            return 'The dog speed is slow'
        elif self.breed.lower() == 'malinois':
            return 'The dog speed is fast'
        elif self.breed.lower() == 'husky':
            return 'The dog speed is very fast'
        else:
            return 'The dog speed is undetermined'
        
# formating a class function        
    def aggression(self):
        if self.breed.lower() == 'bulldog':
           return f'{self.breed} is gentle'
        elif self.breed.lower() == 'chihuahua':
            return f'{self.breed} is gentle'
        elif self.breed.lower() == 'malinois':
            return f'{self.breed} is stubborn'
        elif self.breed.lower() == 'husky':
            return f'{self.breed} is talkative'
        else:
            return 'not determined'
        

dog = Dog('husky',56,'white','female','schophy',1.6,30)
print(dog.breed)
print(dog.run_speed())
print(dog.aggression())



