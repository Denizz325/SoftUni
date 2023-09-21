num_of_people = int(input())
capacity = int(input())

result = num_of_people // capacity

if num_of_people % capacity != 0:
    result += 1

print(result)