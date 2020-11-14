# You may need to check multiple conditions to determine the correct action

country=input('What is your home country: ')
province=input('What is your Province: ')
province=province.capitalize()
if province=='Alberta':
    tax=0.05
    print(tax)
elif province=='Nunavut':
    tax=0.05
    print(tax)
elif province=='Ontario':
    tax=0.13
    print(tax)


# When you use elif instead of multiple 'if' statements you can add a default action

if province=='Alberta':
    tax=0.05
    print(tax)
elif province=='Nunavut':
    tax=0.05
    print(tax)
elif province=='Ontario':
    tax=0.13
    print(tax)
else:
    tax=0.15
    print(tax)


# If multiple conditions cause the same action they can be combined into a single condition

if province=='Alberta' or 'Nunavut':
    tax=0.05
    print(tax)
elif province=='Ontario':
    tax=0.13
    print(tax)
else:
    tax=0.15
    print(tax)


# If you have a list of possible values to check, you can use the IN operator

if province=='Alberta'and 'Nunavut': 
    tax=0.05
    print(tax)
elif province=='Ontario':
    tax=0.13
    print(tax)
else:
    tax=0.15
    print(tax)


# If an action depends on a combination of conditions, you can nest if statements

country=country.capitalize
if country=='Canada':
    if province in('Alberta', 'Nunavut', 'Yukon'):
        tax=0.05
        print(tax)
    elif province=='Ontario':
        tax=0.13
        print(tax)
    else:
        tax=0.15
        print(tax)

else:
    tax=0
    print(tax)
    
