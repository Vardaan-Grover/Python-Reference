fhand = open('C://Users/coolv/Documents/Python/File for Reading.txt', 'r')
# Counting lines in a File
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)