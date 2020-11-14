#SYNTAX ERRORS 
#This code won't run at all 

x=42
y=206
if x==y:
    print('Success')

# RUNTIME ERR0RS
# This code will fail when run

x=42
y=0
print(x/y) 

#LOGIC ERRORS
#This code won't run at all

x=206
y=42
if x<y:
    print(str(x) + 'is greater than '+ str(y))
    