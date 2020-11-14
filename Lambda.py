def sorter(item):
    return item['name']
#Sort Alphabetically
presenters=[
    {'name':'Vardaan', 'age':14},
    {'name':'Aryan', 'age':11}
]
presenters.sort(reverse = True , key=lambda item: item['age'])
print(presenters)

#Sort by length (shortest to longest)

presenters.sort(key=lambda item: len(item['name']))
print('~~~~length~~~~')
print(presenters)