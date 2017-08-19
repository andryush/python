from sys import argv # importing
script, filename = argv # assigning to argv

txt = open(filename) # assign filename to var and perape to open txt. NOT OPENING
print(f'Here is your file: {filename}') # printing assigned filename
print(txt.read()) # printing all that includes txt var

#print('Please type filenema again') # print to user
file_again = input('File name > ') # another way to ask user for file
txt_again = open(file_again) # prepare to open var file_again
print(txt_again.read()) # printing all that includes txt_again var
