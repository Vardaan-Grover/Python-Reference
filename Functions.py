#SOMETIMES WE COPY AND PASTE OUR CODE 

from datetime import datetime
#print timestamps to see how long sections of code 
#take to run 

first_name = 'Susan'
print('task completed')
print(datetime.now())
print()

for x in range(0,10):
    print(x)
    
print('task completed')
print(datetime.now())
print()

#Print the current time 
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

print_time('Kuch Bhi')

for x in range(0,10):
    print(x)
    
print_time('Kuch Bhi')