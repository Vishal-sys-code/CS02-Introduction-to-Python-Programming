import re

# Sample text containing URLs
text = """
Visit our website at https://www.example.com for more information.
You can also check our blog at http://blog.example.com/post/123.
Don't forget to follow us on social media: https://twitter.com/example and https://www.example.org.
Here is an invalid URL: http://.com or https://example..com
"""

# Regex pattern for matching URLs
url_pattern = r'https?://[^\s/$.?#].[^\s]*'

# Find all URLs in the text
urls = re.findall(url_pattern, text)

# Print the extracted URLs
for url in urls:
    print("Found URL:", url)