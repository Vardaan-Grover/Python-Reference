import re as regex

txt = "The rain in Spain"
x = regex.sub("\s", " ", txt)
print(x)

txt = "The rain in Spain"
x = regex.sub("\s", "9", txt, count=2)
print(x)