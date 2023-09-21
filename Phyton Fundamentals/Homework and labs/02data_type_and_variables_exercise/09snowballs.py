snowballs = int(input())

max_weight = 0
max_time = 0
max_value = 0
max_quality = 0

for current_snowball in range(snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    current_value = (snowball_weight / snowball_time) ** snowball_quality

    if current_value > max_value:
        max_weight = snowball_weight
        max_time = snowball_time
        max_value = current_value
        max_quality = snowball_quality

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")