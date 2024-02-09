from collections import deque

worms = deque(int(num) for num in input().split())
holes = deque(int(num) for num in input().split())

matches = 0
no_matches = 0

while worms and holes:
    current_w0rm = worms.pop()

    if current_w0rm <= 0:
        continue

    current_hoe = holes.popleft()

    if current_w0rm == current_hoe:
        matches += 1

    elif current_w0rm != current_hoe:
        worms.append(current_w0rm - 3)
        no_matches += 1

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if len(worms) == 0:
    if no_matches == 0:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")

else:
    print(f"Worms left:", ", ".join([str(worm) for worm in worms]))
if len(holes) == 0:
    print("Holes left: none")
else:
    print(f"Holes left:", ", ".join([str(hole) for hole in holes]))

