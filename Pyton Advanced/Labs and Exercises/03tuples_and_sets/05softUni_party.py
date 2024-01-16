guests = set()

for _ in range(int(input())):
    guest_code = input()
    guests.add(guest_code)


guest_code = input()

while guest_code != "END":
    if guest_code in guests:
        guests.remove(guest_code)

    guest_code = input()

print(len(guests))
for code in sorted(guests):
    print(code)



