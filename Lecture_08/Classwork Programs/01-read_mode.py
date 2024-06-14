import os

print("------ File opening in Reading mode ------")
# The file "file.txt", will be opened with the reading mode
print("--- Example 1 ---")
file = open('read_mode_file.txt', 'r')
# Printing each line one by one in the file
for each in file:
    print(each)

print()
print("--- Example 2 ---")
file = open('read_mode_file.txt', 'r')
print(file.read())

print()
print("--- Example 3 ---")
with open("read_mode_file.txt") as file:  
    data = file.read() 
print(data)

print()
print("--- Example 4 ---")
file = open('read_mode_file.txt','r')
print(file.read(5))