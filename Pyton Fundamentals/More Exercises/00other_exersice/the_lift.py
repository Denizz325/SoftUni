# 01. Programming Fundamentals Mid Exam Retake задача 2

people_waiting = int(input())
lift_state = list(map(int, input().split()))

for wagon_position, current_wagon in enumerate(lift_state):
    available_space = 4 - current_wagon
    if available_space > 0:
        if people_waiting >= available_space:
            lift_state[wagon_position] = 4
            people_waiting -= available_space
            available_space = 0
        else:
            lift_state[wagon_position] += people_waiting
            people_waiting = 0

if people_waiting == 0 and available_space == 0:
    print(*lift_state)

elif sum(lift_state) < len(lift_state) * 4:
    print("The lift has empty spots!")
    print(*lift_state)
else:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*lift_state)


