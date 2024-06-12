# **File Handling**

File handling in python is very powerful adn versatile tool that can be used to perform a wide range of operations. However, it is important to carefully consider the advantages and disadvantages of file handling when writing programns, to ensure that the code is secure, reliable, and performs well.

**Advantages :**
* Versatility
* Flexibility
* User-Friendly
* Cross-Platform

**Disadvantages :**
* Error Prone
* Security risk
* Complexity
* Performance

## **File Operations Mode :**
* **`r`**: Open an existing file for reading.
* **`w`**: Open an existing file for writing but there is a condition in which if the file already exist and contains some data then it will be overridden but if the file is not present then it will create the file as well.
* **`a`**: Open an existing file for append operation. It won't override existing data.
* **`r+`**: To read and write data into the file. The previous data in the file will be overridden.
* **`w+`**: To write and read data. It will override existing data.
* **`a+`**: To append and read data from the file. It won't override existing data.

## **File Open**
At first we need to perform the operation of opening of file, before reading or writing the file.
We have a inbuilt function `open()`.

**Syntax :**

```py
f = open(filename, mode)
```