key = int(input())

lines = int(input())

message = ""

for i in range(lines):

    character = input()
    decrypted = chr(ord(character) + key)
    message += decrypted

print(message)


