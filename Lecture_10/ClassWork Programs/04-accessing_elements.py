dict = {
    1:'Geeks',
    'name': 'GH',
    3:'Hardy'
}

print("\n----- Accessing element using key -----")
print(dict['name'])
print("\n----- Accessing a element using key -----")
print(dict[1])

# Using get() method
dict = {
    1: 'Andrew',
    2:'Huberman',
    3:'Podcasts'
}
print("\n----- Accessing element using key -----")
print(dict.get(2))

# Accessing a Nested Dictionary
dict = {
    'dict1':{
        1: 'Vishal'
    },
    'dict2':{
        'Name':'Stanford'
    }
}
print("\n----- Accessing element in Nested Dictionary -----")
print(dict['dict1'])
print(dict['dict1'][1])
print(dict['dict2']['Name'])
print(dict['dict2'][2])