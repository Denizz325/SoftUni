import re

line = input()
word_to_search = input()
pattern = fr'\b{word_to_search}\b'
#pattern = r'\b' + re.escape(word_to_search) + r'\b'  |  МОЖЕ И ТАКА
matches = re.findall(pattern, line, re.IGNORECASE)
print(len(matches))
