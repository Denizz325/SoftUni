import re

text = input()
pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'
extracted_emails = re.findall(pattern, text)

for extracted_emails in extracted_emails:
    print(extracted_emails[0])