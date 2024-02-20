def tribonacci(num):
    if num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    elif num == 3:
        return [1, 1, 2]

    sequence = [1, 1, 2]
    while len(sequence) < num:
        next_number = sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(next_number)

    return sequence

numbers = int(input())

tribonacci_sequence = tribonacci(numbers)

print(" ".join(map(str, tribonacci_sequence)))
