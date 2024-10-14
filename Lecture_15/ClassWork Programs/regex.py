import re

# Sample text for demonstration
text = "My email is example@example.com. Call me at 123-456-7890!"

# 1. Match a specific word
pattern1 = r'email'
match1 = re.search(pattern1, text)
if match1:
    print("Match Found:", match1.group())

# 2. Find all occurrences of a pattern
pattern2 = r'\d+'  # Matches one or more digits
matches2 = re.findall(pattern2, text)
print("All Digits Found:", matches2)

# 3. Search for an email address
pattern3 = r'\w+@\w+\.\w+'
match3 = re.search(pattern3, text)
if match3:
    print("Email Found:", match3.group())

# 4. Replace a substring
pattern4 = r'Call me at \d+-\d+-\d+'
replacement4 = "Call me at [REDACTED]"
replaced_text = re.sub(pattern4, replacement4, text)
print("Replaced Text:", replaced_text)

# 5. Match and extract a phone number
pattern5 = r'(\d{3})-(\d{3})-(\d{4})'  # Matches phone numbers in the format xxx-xxx-xxxx
match5 = re.search(pattern5, text)
if match5:
    print("Phone Number Found:", match5.group())
    print("Area Code:", match5.group(1))  # First capturing group
    print("Central Office Code:", match5.group(2))  # Second capturing group
    print("Line Number:", match5.group(3))  # Third capturing group

# 6. Validate an email address (basic)
pattern6 = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
email = "test@example.com"
if re.match(pattern6, email):
    print("Valid Email:", email)
else:
    print("Invalid Email:", email)

# 7. Split a string using regex
text_to_split = "apple, orange; banana|grape"
split_pattern = r'[,\s;|]+'  # Matches commas, spaces, semicolons, and pipes
split_result = re.split(split_pattern, text_to_split)
print("Split Result:", split_result)
