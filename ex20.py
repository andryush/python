from sys import argv
script, input_file = argv

def print_all(f): # f is variable and whatever we can pass
    print(f.read()) # reading file

def rewind(f):
    f.seek(0) # seek is for move coursore to begin of the file 0-is a byte

def print_a_line(line_count, f): #line_count is also variable and anything other can pass there
    print(line_count, f.readline()) #readline is reading current line, when print is nothing it means end of file

current_file = open(input_file)

print('First lets print whole file:\n')
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

rewind(current_file)
current_line += 1
print_a_line(current_line, current_file)
