**Exercise 1:** What is the purpose of the “def” keyword in Python?

[] It is slang that means “the following code is really cool”
[] It indicates the start of a function
[] It indicates that the following indented section of code is to be stored for later
[] b and c are both true
[] None of the above

<hr>

**Exercise 2:** What will the following Python program print out?

```py
def fred():
   print("Zap")

def jane():
   print("ABC")

jane()
fred()
jane()
```
[] Zap ABC jane fred jane
[] Zap ABC Zap
[] ABC Zap jane
[] ABC Zap ABC
[] Zap Zap Zap

<hr>

**Exercise 3:** Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
```
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
```

<hr>

**Exercise 4:** Rewrite the grade program from the previous chapter using a function called `computegrade` that takes a score as its parameter and returns a grade as a string.

```
 Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
 < 0.6     F
```
```
Enter score: 0.95
A
```
```
Enter score: perfect
Bad score
```
```
Enter score: 10.0
Bad score
```
```
Enter score: 0.75
C
```
```
Enter score: 0.5
F
```