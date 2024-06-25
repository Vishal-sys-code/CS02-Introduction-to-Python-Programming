print("------- Method 1: Using remove() method -------")
list = [1,2,3,4,5,6,7,8,9,10]
print("Initial List: ")
print(list)
list.remove(5)
list.remove(3)
print("\nList after removing two elements: ")
print(list)

list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
print("Initial List: ")
print(list1)
for i in range(1,5):
    list1.remove(i)
print("\nList after removing two elements: ")
print(list1)

print("-----------------------------------------------")
print("------- Method 2: Using pop() method -------")
list2 = [1,2,3,4,5,6,7,8,9,10]
print("List before popping: ")
print(list2)
list2.pop()
print("\nList after popping: ")
print(list2)
