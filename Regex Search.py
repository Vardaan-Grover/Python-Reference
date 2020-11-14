import re as regex
text='The rain in Spain !'
x = regex.search('^The.*!$', text)
if x:
    print('We have a match !')
else:
    print('Sorry ! No Match')
    
txt = "The rain in Spain"
x = regex.search(" ", txt)
print("The first white-space character is located in position:", x.start())