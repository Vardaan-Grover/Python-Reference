# IMPORTING A MODULE

#import module as namespace
import Helpers
Helpers.display(message= 'Not a warning')

#import all into current namespace
from Helpers import *
display('Not a warning')

#import specific items into current namespace
from Helpers import display 
display('Not a warning')

# INSTALLING PACKAGES



