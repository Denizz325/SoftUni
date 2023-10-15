numbers = [int(num) for num in input().split()]
finish_line_index = len(numbers) // 2
left_car = numbers[:finish_line_index]
right_car = numbers[finish_line_index + 1:]

total_left_car_time = 0
total_right_car_time = 0

for current_time in left_car:
    if current_time == 0:
        total_left_car_time *= 0.8

    total_left_car_time += current_time

for current_time in right_car:
    if current_time == 0:
        total_right_car_time *= 0.8
    total_right_car_time += current_time

if total_right_car_time < total_left_car_time:
    print(f"The winner is {'right'} with total time: {total_right_car_time:.1f}")
else:
    print(f"The winner is {'left'} with total time: {total_left_car_time:.1f}")



