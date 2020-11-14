# We already learned to create function which accept a parameter and return values 
def get_initial(name):
    intitial = name[0:1].upper() 
    return intitial

first_name = input('Enter your first name: ').lstrip()
first_name_intitial = get_initial(name= first_name)

print('Your intitial is: '+ first_name_intitial)

# Functions can accept multiple parameters
 
def get_initial(name, force_uppercase):
    name= name.lstrip()    
    if force_uppercase==True:
        initial= name[0].upper()
    else:
        initial=name[0]
    return initial
        
first_name=input('Enter your first name: ')
first_name_initial=get_initial(name=first_name, force_uppercase= False)

print('Your intitial is: '+ first_name_initial)

# Using named notations when calling functions makes your code more readable

def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('oh no error: ' + error_message)
    #Imagine code here that logs our error to a database or file 
    
first_number = 10 
second_number = 5
if first_name > second_number:
    error_logger(error_code=45, 
                 error_severity=1, 
                 log_to_db= True, 
                 error_message='Second number greater than first', 
                 source_module='my_math_method')
    
    