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

```