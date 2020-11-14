# CLASS METHODS
class Person:
    # This is an attribute, which means that this will not change the instances of the class Person, in the way self.name does.
    number_of_people = 0
    
    def __init__(self, name):
        self.name = name
        Person.add_person(1)

    @classmethod
    def no_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls, add_people):
        cls.number_of_people += add_people

p1 = Person('Vardaan')

p2 = Person('Tim')

print(Person.no_of_people())

#STATIC METHODS

class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        return 'run'

print(Math.add5(5))
print(Math.pr())