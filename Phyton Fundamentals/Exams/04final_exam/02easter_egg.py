import re

text = input()
eggs = {}

pattern = r'([\@#{1,}]+)([a-z]{3,})([\@#{1,}]+)([*$%^&*\])?([\/]+)([\d]+)([\/]+)'

matches = re.finditer(pattern, text)

for match in matches:
    color = match.group(2)
    number = match.group(5)
    eggs[color] = number

for color, number in eggs.items():
    print(f'You found {number} {color} eggs!')

