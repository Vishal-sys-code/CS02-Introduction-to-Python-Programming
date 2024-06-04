# **Identation**
This is the very important part specially in python language. 

* Increase indent after an `if` or `for` statement [after :]
* Maintain indent to indicate the scope of the block.
* Reduce indent back to the level of the `if` or `for` statement to indicate that the end of the block.
* Blank lines are ignored
* Comment on a line by themselves are ignored with regard to the identation.

**Example:**
```py
x = 5
if x > 2:
    print('Bigger than 2')
    print('Still Bigger')
print('Done with 2')

for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')
```