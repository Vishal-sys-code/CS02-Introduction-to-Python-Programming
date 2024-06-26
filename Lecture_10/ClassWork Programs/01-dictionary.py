dict = {
    1: "Apple", 
    2: "Microsoft",
    3: "Google"
}

dict_1 = {
    "Name": "Vishal",
    "Number": [1,2,3],
    1: [1,2,3,4,5,6]
}

print("------ Dictionary with use of integer keys ------")
print(dict)
print("------ Dictionary with use of multiple keys ------")
print(dict_1)

dict_2 = {}
print("Empty Dictionary")
print(dict_2)
dict_3 = dict({1:'Geeks', 2:'Nerds', 3:'Introverts'})
print("\n Dictionary with the use of the dict(): ")
print(dict_3)
dict_4 = dict([(1,'Geeks'), (2, 'Nerds'), (3, 'Introverts')])
print("\nDictionary with each item as a pair: ")
print(dict_4)