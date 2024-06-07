# **Nested Loops**
The "inner Loop" will finish all of its iteration before finishing one iteration of the "outer loop".

**Example :**
```py
row = int(input("Enter the Rows: ""))
cols = int(input("Enter the Columns :"))
symbol = input("Enter the symbol :")

for i in range(row):
    for j in range(cols):
        print(symbol)
    print()
```
