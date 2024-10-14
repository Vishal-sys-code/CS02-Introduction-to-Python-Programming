# Regular Expressions

## Introduction to Regular Expressions
Regular expressions (regex) are powerful tools for searching, matching, and manipulating strings based on specific patterns. In Python, the `re` module provides functions for working with regex.

**What is a Regular Expression?**
A regular expression is a sequence of characters that define a search pattern. This pattern can be used for various tasks such as validating input, searching for specific strings, or replacing parts of strings.

**Basic Syntax :**
Here's a brief overview of some common regex components:

* Literals: Match the exact characters (e.g., `hello` matches "hello").
* Metacharacters: Characters with special meanings, such as:
    * `.`: Matches any single character.
    * `^`: Matches the start of a string.
    * `$`: Matches the end of a string.
    * `*`: Matches 0 or more repetitions of the * preceding element.
    * `+`: Matches 1 or more repetitions of the preceding element.
    * `?`: Matches 0 or 1 occurrence of the preceding element.
    * `[]`: Matches any single character within the brackets (e.g., [abc] matches "a", "b", or "c").
    * `|`: Acts like a logical OR (e.g., abc|def matches either "abc" or "def").

## **The `re` Module**
To work with regular expressions in Python, you need to import the `re` module.

```py
import re
```

**Common Functions**
* `re.match()`: Determines if the regex matches at the beginning of the string.
* `re.search()`: Searches the entire string for a match.
* `re.findall()`: Returns a list of all matches in the string.
* `re.sub()`: Replaces occurrences of the regex with a specified replacement.


## **Basic Examples**

### Matching with `re.match()`
```py
import re

pattern = r'hello'
string = 'hello world'

match = re.match(pattern, string)
if match:
    print("Match found:", match.group())
else:
    print("No match")
```

### Searching with `re.search()`
```py
import re

pattern = r'world'
string = 'hello world'

search = re.search(pattern, string)
if search:
    print("Search found:", search.group())
else:
    print("No search found")
```

### Finding All Matches with `re.findall()`
```py
import re

pattern = r'\d+'  # Matches one or more digits
string = 'I have 2 apples and 3 oranges.'

matches = re.findall(pattern, string)
print("All matches:", matches)  # Output: ['2', '3']
```
### Replacing with `re.sub()`
```py
import re

pattern = r'apples'
replacement = 'bananas'
string = 'I have apples and oranges.'

new_string = re.sub(pattern, replacement, string)
print("Replaced string:", new_string)  # Output: I have bananas and oranges.
```

## **Advanced Patterns**
* **Lookaheads:** Assert that a pattern is followed by another without including it. `Syntax`: `X(?=Y)` (e.g., r'cats(?= and)').
**Lookbehinds:** Assert that a pattern is preceded by another. `Syntax`: `(?<=Y)X` (e.g., r'(?<=email is )\w+@\w+\.\w+').
**Non-capturing Groups:** Group patterns without capturing them for backreferencing. `Syntax`: `(?:...)` (e.g., r'(?:apples|oranges)').
**Named Groups**: Assign names to capturing groups for easier access. `Syntax`: `(?P<name>...)` (e.g., r'(?P<fruit>apples) is \$(?P<price>\d)').
**Backreferences:** Reference a previously captured group. `Syntax`: `\n` where `n` is the group number (e.g., r'(\b\w+) \1').
**Verbose Mode**: Write regex with whitespace and comments for readability. Use `re.VERBOSE` (e.g., r"""\b(cat|dog)\b""").
**Flags:** Modify regex behavior (e.g., `re.IGNORECASE` for case-insensitive matching).

```py
import re

text = """I love cats and dogs.
My email is test@example.com.
The price of apples is $3 and oranges is $2.
Hello World
hello world
abc abcd abcde"""

# 1. Lookaheads
lookahead_pattern = r'cats(?= and)'
lookahead_match = re.search(lookahead_pattern, text)
if lookahead_match:
    print("Lookahead Found:", lookahead_match.group())

# 2. Lookbehinds
lookbehind_pattern = r'(?<=email is )\w+@\w+\.\w+'
lookbehind_match = re.search(lookbehind_pattern, text)
if lookbehind_match:
    print("Lookbehind Found:", lookbehind_match.group())

# 3. Non-capturing Groups
non_capturing_pattern = r'(?:apples|oranges)'
non_capturing_matches = re.findall(non_capturing_pattern, text)
print("Non-capturing Groups Found:", non_capturing_matches)

# 4. Named Groups
named_group_pattern = r'(?P<fruit>apples|oranges) is \$(?P<price>\d)'
named_group_matches = re.finditer(named_group_pattern, text)
for match in named_group_matches:
    print(f"Named Group Found: {match.group('fruit')} costs ${match.group('price')}")

# 5. Backreferences
backreference_pattern = r'(\b\w+) \1'
backreference_matches = re.finditer(backreference_pattern, text)
for match in backreference_matches:
    print("Backreference Found:", match.group())

# 6. Verbose Mode
verbose_pattern = re.compile(r"""
    \b         # Word boundary
    (cat|dog)  # Match 'cat' or 'dog'
    \b         # Word boundary
""", re.VERBOSE)

verbose_matches = verbose_pattern.findall(text)
print("Verbose Mode Found:", verbose_matches)

# 7. Flags
flag_pattern = r'hello'
flag_matches = re.findall(flag_pattern, text, re.IGNORECASE)
print("Flags Found:", flag_matches)
```