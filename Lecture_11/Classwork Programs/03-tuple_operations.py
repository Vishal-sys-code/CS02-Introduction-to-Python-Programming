# CONCATENATION
tuple1 = (0,1,2,3)
tuple2 = ("Python", "Java")
print("------ Concatenation of Tuples: ------")
print(tuple1 + tuple2)

# ------------------------------------------------------------------------------------------------

# NESTING
# It means a tuple inside another tuple
tuple1 = (0,1,2,3)
tuple2 = ("Python", "Java")
tuple3 = (tuple1, tuple2)
print("\n------ Nesting of Tuples: ------")
print(tuple3)

# ------------------------------------------------------------------------------------------------

# REPETITION
# We can create a tuple of multiple same elements from a single element in that tuple
tuple1 = ("python",)*3
print("\n------ Repetition of Tuples: ------")
print(tuple1)

# ------------------------------------------------------------------------------------------------

# SLICING
# Dividing the tuples into small tuples using indexing methods
tuple1 = (0,1,2,3,4,5,6,7)
print("\n------ Slicing of Tuples: ------")
print(tuple1[0:3])
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])

# ------------------------------------------------------------------------------------------------

# DELETING
# Use 'del' keyword for deleting a tuple. The output will be in the form of error because after deleting the tuple it will give a NameError. 
tuple1 = (0,1,2,3,4,5,6,7)
del tuple1
print("\n------ Deleting of Tuples: ------")
# print(tuple1) # NameError: name 'tuple1' is not defined. Did you mean: 'tuple2'?

# ------------------------------------------------------------------------------------------------

# LENGTH OF THE TUPLE
tuple1 = (0,1,2,3,4,5,6,7)
print("\n------ Length of the Tuple: ------")
print(len(tuple1))
tuple2 = ('Java', 'C++')
print(len(tuple2))

# ------------------------------------------------------------------------------------------------

# CONVERTING LIST INTO TUPLES
# We can do this by using a tuple() constructor and passing the list as its parameter.
list1 = [0,1,2]
print("\n----- Converting List into the Tuples: ------")
print(tuple(list1))
print(tuple('python'))

# ------------------------------------------------------------------------------------------------

# MULTI-DATATYPES
tuple = ("immutable", True, 12)
print("\n----- Multi-Datatypes: ------")
print(tuple)

# ------------------------------------------------------------------------------------------------

# TUPLES IN A LOOP
# We can create a tuple with a single element in it using loops.

tuple = ("Python",)
n = 5
print("\n----- Tuples in a Loop -----")
for i in range(n):
    tup = (tuple,)
    print(tup)