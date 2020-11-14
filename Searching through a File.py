fhand = open('C://Users/coolv/Documents/Python/File for Reading.txt', 'r')

for line in fhand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)

# Skipping lines with continue
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From: '):
        continue
    print(line)

# Finding specific elements in lines
for line in fhand:
    if not '@uct.ac.za' in line:
        continue
    print(line)