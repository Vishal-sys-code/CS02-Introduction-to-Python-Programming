list = ['M','A', 'C', 'H', 'I', 'N', 'E', 'L', 'E', 'A', 'R', 'N', 'I', 'N', 'G', 'A', 'T', 'C', 'O', 'L', 'L', 'E', 'G', 'E']
print("Initial List: ")
print(list)

sliced_list = list[3:8]
print("\nElements sliced from the range of the 3 to 8: ")
print(sliced_list)

sliced_list_1 = list[5:]
print("\nElements sliced from 5th element till the end: ")
print(sliced_list_1)

sliced_list_2 = list[:]
print("\nPrinting all the elements using slice operations: ")
print(sliced_list_2)

# NEGATIVE INDEXING
sliced_list_3 = list[:-6]
print("\nElements sliced from the beginning till the 6th element from the end: ")
print(sliced_list_3)

sliced_list_4 = list[-6 : -1]
print("\nElements sliced from the 6th element from the end till the 2nd last element: ")
print(sliced_list_4)

sliced_list_5 = list[::-1]
print("\nElements sliced in reverse order: ")
print(sliced_list_5)