import re

line = input()
word_to_search = input()
regex = r'\b' + re.escape(word_to_search) + r'\b'
matches = re.findall(regex, line, re.IGNORECASE)

print(len(matches))
