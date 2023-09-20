word = input()
indexes_of_uppercase = []

for i in range(len(word)):
    if word[i].isupper():
        indexes_of_uppercase.append(i)



print(indexes_of_uppercase)
