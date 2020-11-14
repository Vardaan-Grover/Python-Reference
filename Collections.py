#Lists are collection of items

names=['Christopher', 'Susan']
scores=[]
scores.append(98) #Add a new item to the end
scores.append(99)
print(names)
print(scores)
print(scores[1]) #Collections are zero-indexed

#Array are also collections of items

from array import array
marks = array('d')
marks.append(97)
marks.append(98)
print(marks)
print(marks[1])

# Common Operations

names=['Susan', 'Christopher']
print(len(names)) # Get the number of items
names.insert(0, 'Bill') # Insert before Index
print(names)
names.sort()
print(names)

# RETRIEVING RANGES

names = ['Susan', 'Christopher', 'Bill', 'Justin']
presenters = names[1:3]
#Start and End Index 

print(names)
print(presenters)

#DICTIONARIES
person = {'first':'Christopher'}
person['last']='Harrison'
print(person)
print(person['first'])    