n = int(input())
unique_elements_set = set()

for i in range(n):
    compounds = input().split()
    unique_elements_set.update(compounds)


for element in unique_elements_set:
    print(element)





