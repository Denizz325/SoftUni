numbers = [int(num) for num in input().split()]
number_k = int(input())

result = []
index = 0

while numbers:
    index = (index + number_k - 1) % len(numbers)
    executed = numbers.pop(index)
    result.append(executed)

result_str = "[" + ",".join(map(str, result)) + "]"
print(result_str)