numbers = [int(num) for num in input().split()]
list_with_popped_nums = []
index = int(input())
while len(numbers) != 0:

    if index < 0:
        pass
    elif index > numbers[-1]:
        pass
    else:
        popped_value = numbers.pop(index)
        list_with_popped_nums.append(popped_value)
        for current_num in numbers:
            if current_num < popped_value:
                current_num += popped_value
                if popped_value in numbers:
                    index = numbers.index(popped_value)
                    numbers[index] = current_num
            else:
                current_num -= popped_value

    index = int(input())
print(numbers)