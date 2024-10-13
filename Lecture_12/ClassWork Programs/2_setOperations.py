mySet = {1,2,3,4,5}
print("Before any operation the Original Set is: ", meSet)

mySet.add(6)
print("After adding an element to the set, the set is: ", mySet)

mySet.remove(3)# Raises KeyError if 3 is not present
print("After removing an element from the set, the set is: ", mySet)

# Using discard to remove without error
my_set.discard(7)  # Does nothing if 7 is not present
print("After discarding 7:", my_set)

# Union, Intersection and Difference Operations
set_a = {1,2,3}
set_b = {3,4,5}
union_set = set_a | set_b
print("Union: ", union_set)
intersection_set = set_a & set_b
print("Intersection: ", intersection_set)
difference_set = set_a - set_b
print("Difference (set_a - set_b)", difference_set)

# Checking Membership
print("Is 2 in a set_a", 2 in set_a)
print("Is 3 in a set_a", 3 in set_b)

# Iterating over a set
print("Iterating over the Set: ")
for element in mySet:
    print("Element: ", element)

# Set comprehension
squares = {x**2 for x in range(1,6)}
print("Set of squares: ", squares)

# Checking subset and superset
set_x = {1,2}
set_y = {1,2,3,4}
print("Is set_x a subset of set_y?", set_x.issubset(set_y))
print("Is set_y a superset of set_x?", set_y.issuperset(set_x))

# Clearing all elements from a set
my_set.clear()
print("After clearing my_set:", my_set)