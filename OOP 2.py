class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print('Meow')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Bark')

# Inheritance

# Upper Level Class / Super Class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')

    def speak(self):
        print('I dont know what to say')

#Child Classes
class Dog(Pet):
    def speak(self):
        print('Bark')

class Cat(Pet):
    def __init__(self, name, age, color):
        self.color = color
        super().__init__(name, age) # What this statement does is that it takes the following arguments from the super class that is Pet and runs them for the child class, which in this case is Cat

    def speak(self):
        print('Meow')

    def show(self):
        print(f'I am {self.name}. I am {self.age} years old and I am {self.color} in color.')

class Fish(Pet):
    pass

p = Pet('Tim', 11)
p.show()
p.speak()

print()

c = Cat('Mitten', 9, 'Black')
c.show()
c.speak()

print()

d = Dog('Bob', 14)
d.show()
d.speak()

print()

f = Fish('Bubbles', 10)
f.show()
f.speak()