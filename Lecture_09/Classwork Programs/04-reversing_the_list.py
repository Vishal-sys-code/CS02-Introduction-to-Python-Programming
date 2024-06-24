print("------ Example 1: Using reverse() method ------")
mylist = [1,2,3,4,5,'Meta', 'Microsoft']
mylist.reverse()
print(mylist)

print("------ Example 2: Using reversed() function ------")

"""
NOTES: 
The `reversed()` function returns a reverse iterator, 
which can be converted to a lost using the `list()` 
function.
"""
mylist = [1,2,3,4,5]
reversed_list = list(reversed(mylist))
print(reversed_list)