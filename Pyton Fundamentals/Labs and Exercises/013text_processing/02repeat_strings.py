words = input().split()
result = " "
for word in words:
    lenght = len(word)
    result += word * lenght

print(result)