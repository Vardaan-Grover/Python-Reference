#WE OFTEN NEED CURRENT DATE AND TIME WHEN LOGGING ERRORS AND SAVING DATA 
#To get current date and time 
#We need to use the datetime library

from datetime import datetime, timedelta, date
current_date= datetime.now()

#The now function returns a datetime object

print('Today is: '+ str(current_date))

#THERE ARE FUNCTIONS YOU CAN USE WITH DATETIME OBJECTS TO MANIPULATE DATES
from datetime import datetime, timedelta, date, time
today = datetime.now()
print('Today is: '+ str(today))

#timedelta is used to define a period of time 

one_day=timedelta(days=1)
yesterday= today - one_day
print('Yesterday was: '+ str(yesterday))

#USE DATE FUNCTIONS TO CONTROL DATE FORMATTING

from datetime import datetime, timedelta
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

birthday= input('When is your birthday (dd/mm/yy): ')
birthday_date= datetime.strptime(birthday, '%d/%m/%y')
print('Birthday: '+ str(birthday_date))
one_day=timedelta(days=1)
birthday_eve=birthday_date-one_day
print('Day before birthday: '+ str(birthday_eve))
