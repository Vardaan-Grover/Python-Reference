import re as regex

text='The media has claimed that the rain in Spain is in pain !'
x=regex.findall('ai', text)
print(x)