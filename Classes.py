#Creating a class
class Human():
    '''
    The __init__ is a sort of a method but is known as a constructor. It is responsible for the making a copy of the class 
    which inherits/contains all the class variables and methods.
    '''
    def __init__(self, name, age, gender):
        self.name = name # This is a field. It stores data and methods to define the behaviour of the class.
        self.age = age
        self.gender = gender
    def say_hello(self):    #<----This was a method. It performs a specific task. Consider it as a function.
        '''
        This function wishes the user with a greeting. Output = Hello Aryan(self.name)
        '''
        print('Hello '+ self.name)
    def tell_age(self): # This was a method as well.
        '''
        This function tells the user the given age. Output = Your age is 11(self.age)
        '''
        print('Your age is '+self.age)
    def tell_gender(self):
        '''
        This function tells the user the given gender. Output = Your gender is Male(self.gender)
        '''
        print('Your gender is '+ self.gender)


person = Human('Vardaan','14','Male')
person.name = 'Aryan'
person.age = '11'
person.gender = 'Female'
person.say_hello()
person.tell_gender()
person.tell_age()