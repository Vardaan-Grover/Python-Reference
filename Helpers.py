# FUNCTION STORED IN A MODULE
from colorama import init, Fore


def display(message, is_warning= False):
    if is_warning==True:
        print('Warning !!!')
    else:
        print(Fore.BLUE + message)