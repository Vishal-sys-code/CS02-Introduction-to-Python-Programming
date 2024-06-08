# **Strings**
It is the collection of the characters surrounded by single, doubles, triple quotes. Each character is encoded in the ASCII. 

**REMEMBER:** Python does not have a character data type, a single character is simply a string with a length of 1.

**Create a String in Python**
Strings in Python can be created using single quotes or double quotes or even triple quotes.

```py
str = 'Hello World'
str_1 = "Hello World"
str_2 = '''Hello World'''

type(str)
type(str_1)
type(str_2)
```

```py
# Creating string with a single quotes
string1 = 'Welcome to the Cambridge University'
print("String with the use of Single Quotes: ")
print(string1)

string2 = "I'm a Professor"
print("\nString with the use of Double Quotes: ")
print(string2)

string3 = '''I'm a part-time professor who comes to show the world of computer science'''
print("\nString with the use of the Triple Quotes: ")
print(string3)

string4 = '''I am 
            a Machine Learning Engineer
            and your mentor'''
print("\nCreating a multiline String: ")
print(string4)
```

## **Accessing characters in Python String**

The individual characters of a String can be accessed by using the method of Indexing. Indexing allows negative address references to access characters from the back of the String, e.g. -1 refers to the last character, -2 refers to the second last character, and so on. 

```sh
C A M B R I D G E
0 1 2 3 4 5 6 7 8
9 8 7 6 5 4 3 2 1 [all are in negative: -9,-8,-7,-6,-5,-4,-3,-2,-1]
```

**Positive Indexing Code :**
```py
string1 = "CAMBRIDGE"
print("The string is: " + string1)
# print("First character: " + string1[0])
# print("Second character: " + string1[1])
# print("Third character: " + string1[2])
# print("Fourth character: " + string1[3])
# print("Fifth character: " + string1[4])
# print("Sixth character: " + string1[5])
# print("Seventh character: " + string1[6])
# print("Eight character: " + string1[7])
# print("Ninth character: " + string1[8])
# print("Tenth character: " + string1[9])

try:
    print("First character: " + string1[0])
    print("Second character: " + string1[1])
    print("Third character: " + string1[2])
    print("Fourth character: " + string1[3])
    print("Fifth character: " + string1[4])
    print("Sixth character: " + string1[5])
    print("Seventh character: " + string1[6])
    print("Eight character: " + string1[7])
    print("Ninth character: " + string1[8])
    print("Tenth character: " + string1[9])
except IndexError:
    print("Invalid Index")
```

**Negative Indexing Code :**

```py
string1 = "CAMBRIDGE"
print("The string is: " + string1)
print("ALL THE CHARACTER WHICH ARE BEING DISPLAYING IS IN THE REVERSE ORDER")
# print("First character: " + string1[-1])
# print("Second character: " + string1[-2])
# print("Third character: " + string1[-3])
# print("Fourth character: " + string1[-4])
# print("Fifth character: " + string1[-5])
# print("Sixth character: " + string1[-6])
# print("Seventh character: " + string1[-7])
# print("Eight character: " + string1[-8])
# print("Ninth character: " + string1[-9])
# print("Tenth character: " + string1[-10])

try:
    print("First character: " + string1[-1])
    print("Second character: " + string1[-2])
    print("Third character: " + string1[-3])
    print("Fourth character: " + string1[-4])
    print("Fifth character: " + string1[-5])
    print("Sixth character: " + string1[-6])
    print("Seventh character: " + string1[-7])
    print("Eight character: " + string1[-8])
    print("Ninth character: " + string1[-9])
    print("Tenth character: " + string1[-10])
except IndexError:
    print("Invalid Index")
```

# **String Slicing**
The method is used to access a range of character in the string. Slicing in a string is done by using a slicing operator i.e. a colon(`:`).
To be honest, it creates a substring by extracting elements from another string indexing ir slicing.

```sh
INDEXING: [start : stop : step]
```
**Example:**

```py
name = "Lana Del Ray"

first_name = name[0]
print(first_name)

first_name_i1 = name[0:1]
first_name_i2 = name[0:2]
first_name_i3 = name[0:3]
first_name_i4 = name[0:4]
first_name_i5 = name[0:5]
first_name_i6 = name[0:6]
first_name_i7 = name[0:7]
first_name_i8 = name[0:8]
first_name_i9 = name[0:9]
first_name_i10 = name[0:10]
first_name_i11 = name[0:11]
first_name_i12 = name[0:12]

print("---- Indexing: (where start is 0)----")
print("first_name_i1: " + first_name_i1)
print("first_name_i2: " + first_name_i2)
print("first_name_i3: " + first_name_i3)
print("first_name_i4: " + first_name_i4)
print("first_name_i5: " + first_name_i5)
print("first_name_i6: " + first_name_i6)
print("first_name_i7: " + first_name_i7)
print("first_name_i8: " + first_name_i8)
print("first_name_i9: " + first_name_i9)
print("first_name_i10: " + first_name_i10)
print("first_name_i11: " + first_name_i11)
print("first_name_i12: " + first_name_i12)

print("----- Indexing: (where start and end both will be taken) -----")
first_name_j1 = name[1:2]
first_name_j2 = name[2:3]
first_name_j3 = name[3:4]
first_name_j4 = name[4:5]
first_name_j5 = name[5:6]
first_name_j6 = name[7:8]
first_name_j7 = name[8:9]

print("first_name_j1: " + first_name_j1)
print("first_name_j2: " + first_name_j2)
print("first_name_j3: " + first_name_j3)
print("first_name_j4: " + first_name_j4)
print("first_name_j5: " + first_name_j5)
print("first_name_j6: " + first_name_j6)
print("first_name_j7: " + first_name_j7)

print("----- Having fun with slicing -----")
funky_name_1 = name[0:8:1]
funky_name_2 = name[0:8:2]
funky_name_3 = name[0:8:3]

print("funky_name_1: " + funky_name_1)
print("funky_name_2: " + funky_name_2)
print("funky_name_3: " + funky_name_3)
```