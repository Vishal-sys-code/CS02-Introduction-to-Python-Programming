import re

# Sample emails for validation
emails = [
    "test@example.com",
    "user.name@domain.co",
    "invalid-email@.com",
    "another.invalid@domain",
    "valid.email+filter@example.com",
    "user@subdomain.domain.com",
    "user@domain..com"  # Invalid
]

# Regex pattern for validating email addresses
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Validate each email
for email in emails:
    if re.match(email_pattern, email):
        print(f"Valid Email: {email}")
    else:
        print(f"Invalid Email: {email}")