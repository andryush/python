from os.path import exists

print('\n***Hi. I\'m a program which can help you to\ntransfer data from one file to another***')
filename1 = input('Please type file name FROM wich you wnat to transfer data > ')

print(f'Excellent, input file is {len(filename1)} bytes long')
filename2 = input('Please type file name where you want to copy data from first file > ')

print(f'Is the output file {filename2} exists? - {exists(filename2)}')
input(f'Okay, i will transfer data from {filename1} to {filename2}\nIf you agree please press ENTER ')

open_file_1 = open(filename1).read() # added .read()
#read_file_1 = open_file_1.read()


open_file_2 = open(filename2, 'w').write(open_file_1)
#open_file_2.write(open_file_1) # changed var in ()

#open_file_1.close()
#open_file_2.close()


print(f'Great, work has done, you can check {filename2} =)' )
