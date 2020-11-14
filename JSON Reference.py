import json

#You can create "Key":"Value" JSON objects from a dictionary
#Create a Dictionary object
person_dict = {'first':'Vardaan', 'second':'Grover'}

#Add additional key pairs as needed to dictionary
person_dict['DOB']='27/08/05'

#Convert dictionary to JSON object
person_json = json.dumps(person_dict)
print(person_json)

#Nest Dictionaries to create JSON in the format
#{"key":{"subkey0":"subvalue0", "subkey1":"subvalue1", .....}}
person_dict1 = {'first':'Vardaan', 'second':'Grover'}

#Creating a staff dictionary which assigns a person to a role 
staff_dict = {}
staff_dict['Program Manager']=person_dict1

#Converting dictonary to JSON object 
staff_json = json.dumps(staff_dict)

#Print JSON Object
print(staff_json)

#Add lists to the dictionary to create JSON in the format
#{"key":["listvalue0", "listvalue1", "listvalue2", .....]}
person_dict2 = {'first':'Vardaan', 'second':'Grover'}

#Create a list of objects of programming languages
languages_list = ['Csharp', 'Python', 'JavaScript', 'Ruby', 'C++']

#Add list to dictionary
person_dict2['languages'] = languages_list

#Convert dictionary to JSON object
person_json1 = json.dumps(person_dict2)

#Print JSON object
print(person_json1)