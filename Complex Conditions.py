# Sometimes you can combine conditions with AND instead of nesting if statements

gpa=input('What is your gpa: ')
lowest_grade=input('What is your lowest grade: ')
gpa=float(gpa)
lowest_grade=float(lowest_grade)

if gpa>=.85 and lowest_grade>=.70:
        print('Well Done !!!')


#If you need to remember the result of a condition, check later in your code, use Boolean variables as flags

if gpa>=.85 and lowest_grade>=.70:
    honour_roll=True
else:
    honour_roll=False
#Somewhere later in the code 

if honour_roll==True:
    print('Well Done !!!')

        