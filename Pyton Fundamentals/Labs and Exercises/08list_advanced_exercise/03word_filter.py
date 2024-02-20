some_text = [current_text  for current_text in input().split() if len(current_text) % 2 == 0]

for word in some_text:
    print(word)