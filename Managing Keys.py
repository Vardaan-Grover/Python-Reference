#Reading an Environment Variable
import os
os_version = os.getenv('PSModulePath')
print(os_version)

# USING DOTENV
# Store environmental variables in text file
# .env file in reference to subcription key
# subsciption_key = bla_bla_bla_bla

from dotenv import load_dotenv
load_dotenv('C:/Users/coolv/Documents/Python/VSC/Key.env')
password = os.getenv('Subscription_Key')
print(password) 
