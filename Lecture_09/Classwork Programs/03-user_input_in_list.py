# Example - 1 
string = input("Enter Elements: ")
list = string.split()
print("List is: ", list)

# Example - 2
n = int(input("Enter the size of the list: "))
lst = list(map(int,input("Enter the integer elements: ").strip().split()))[:n]
print("List is: ", lst)

# Example - 3
lst = []
n = int(input("Enter the number of elements: "))
for i in range(0,n):
    element = int(input())
    lst.append(element)
print(lst)

# Example - 4
lst = []
n = int(input("Enter the number of elements: "))
for i in range(0,n):
    element = [input(), int(input())]
    lst.append(element)
print(lst)

# There are two in-built functions through which we can insert the elements at the end of the list, the functions are:- `append()` and `extend()`
list = []
list.append(1)
list.append(2)
list.append(3)
for i in range(1,4):
    list.append(i)

list2 = ["Fydor", "Dostoevsky"]
list.append(list2) # Adding list in a list