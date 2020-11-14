# This function will take a name and return the first letter of the name
def get_initial(name, force_uppercase=True):
    name= name.lstrip()
    if force_uppercase==True:
        initial= name[0].upper()
    else:
        initial= name[0]
    return initial

# Ask for someone's name and return their initials
first_name=input('Enter your first name: ')
first_name_initial= get_initial(name= first_name, force_uppercase= False)


print('Your initial is: '+ first_name_initial)