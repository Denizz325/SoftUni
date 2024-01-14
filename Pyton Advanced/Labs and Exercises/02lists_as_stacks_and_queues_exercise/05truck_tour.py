from collections import deque

pumps = deque([[int(num) for num in input().split()]for _ in range(int(input()))])

pumps_copy = pumps.copy()
gas_in_tank = 0
index = 0

while pumps_copy:
    petrol, distance = pumps_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -= distance

    else:
        pumps.rotate(-1)