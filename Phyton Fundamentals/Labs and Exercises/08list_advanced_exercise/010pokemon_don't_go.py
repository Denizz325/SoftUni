numbers = [int(num) for num in input().split()]
list_with_popped_nums = []

while True:

    if len(numbers) == 0:
        break
    index = int(input())

    if index < 0:
        index = 0
        popped_value = numbers.pop(index)
        list_with_popped_nums.append(popped_value)
        last_element = numbers[-1]
        numbers.insert(0, last_element)
        for i in range(len(numbers)):
            if numbers[i] <= popped_value:
                numbers[i] += popped_value
            else:
                numbers[i] -= popped_value

    elif index > len(numbers) - 1:
        index = len(numbers) - 1
        popped_value = numbers.pop(index)
        list_with_popped_nums.append(popped_value)
        first_element = numbers[0]
        numbers.append(first_element)
        for i in range(len(numbers)):
            if numbers[i] <= popped_value:
                numbers[i] += popped_value
            else:
                numbers[i] -= popped_value
    else:
        popped_value = numbers.pop(index)
        list_with_popped_nums.append(popped_value)
        for i in range(len(numbers)):
            if numbers[i] <= popped_value:
                numbers[i] += popped_value
            else:
                numbers[i] -= popped_value

result = sum(list_with_popped_nums)
print(result)