# stack = []
# opening_brackets = {'(', '[', '{'}
# closing_brackets = {')': '(', ']': '[', '}': '{'}
#
# input_sequence = input()
#
# for char in input_sequence:
#     if char in opening_brackets:
#         stack.append(char)
#     elif char in closing_brackets:
#         if not stack or stack.pop() != closing_brackets[char]:
#             print("NO")
#             break
# else:
#     print("YES" if not stack else "NO")

from collections import deque

parenthesis = deque(input())  # ["(", "{", ...]
open_parenthesis = deque()

while parenthesis:
    current_parenthesis = parenthesis.popleft()

    if current_parenthesis in "({[":
        open_parenthesis.append(current_parenthesis)
    elif not open_parenthesis:
        print("NO")
        break
    else:
        if f"{open_parenthesis.pop() + current_parenthesis}" not in "()[]{}":
            print("NO")
            break
else:
    print("YES")