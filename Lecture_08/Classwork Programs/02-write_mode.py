# Example - 1 
 
print("Example - 1")
file = open('write_mode_file.txt', 'w')
file.write("Hi, This is the write command")
file.write("Nice to meet you")
file.write("It allows us to write in a particular file")
file.close()


# Example - 2
print("Example - 2")
with open('write_mode_file.txt','w') as f:
    f.write("Hi, I am written statement along with the with() method or statement")
