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