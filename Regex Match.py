import re as regex 

txt = "The rain in Spain"
x = regex.search("ai", txt)
print(x) #this will print an object

#The regular expression looks for any words that starts with an upper case "S"
txt = "The rain in Spain"
x = regex.search(r"\bS\w+", txt)
print(x.span())

#Print the string passed into the function
txt = "The rain in Spain"
x = regex.search(r"\bS\w+", txt)
print(x.string)

#Print the part of the string where there was a match.
#The regular expression looks for any words that starts with an upper case "S"
txt = "The rain in Spain"
x = regex.search(r"\bS\w+", txt)
print(x.group())