name_1 = "Elon Musk"
name_2 = "ksuM nolE"
name_3 = "Andrew Huberman"
name_4 = "namrebuH werdnA"

print("----- Reversing the strings -----")
print("Reversed name_1: " + name_1[::-1])
print("Reversed name_2: " + name_2[::-1])
print("Reversed name_3: " + name_3[::-1])
print("Reversed name_4: " + name_4[::-1])

print("----- Built-in reverse a string -----")
name_1_builtin_reverse = "".join(reversed(name_1))
name_2_builtin_reverse = "".join(reversed(name_2))
name_3_builtin_reverse = "".join(reversed(name_3))
name_4_builtin_reverse = "".join(reversed(name_4))
print("Reversed name_1: " + name_1_builtin_reverse[::-1])
print("Reversed name_2: " + name_2_builtin_reverse[::-1])
print("Reversed name_3: " + name_3_builtin_reverse[::-1])
print("Reversed name_4: " + name_4_builtin_reverse[::-1])