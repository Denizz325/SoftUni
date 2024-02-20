def is_palindrom(some_number: str) -> bool:
    if some_number == some_number[::-1]:
        return True
    return False


number_as_str = input().split(", ")
for number in number_as_str:
    print(is_palindrom(number))
