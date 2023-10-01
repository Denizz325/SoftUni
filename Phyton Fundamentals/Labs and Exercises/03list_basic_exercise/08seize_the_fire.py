fire_cells = input().split("#")
water_as_int = int(input())

total_effort = 0
total_fire = 0

list_with_cells = []


for current_fire_cell in fire_cells:
    splited_fire_cells = current_fire_cell.split(" = ")
    type_of_fire = splited_fire_cells[0]
    value_of_cell = int(splited_fire_cells[1])

    if water_as_int < value_of_cell:

        break
    if value_of_cell < 1 or value_of_cell > 125:
        continue

    if type_of_fire == "High" and 81 <= value_of_cell <= 125:
        water_as_int -= value_of_cell
        total_effort += value_of_cell * 0.25
        total_fire += value_of_cell
        list_with_cells.append(value_of_cell)

    elif type_of_fire == "Medium" and 51 <= value_of_cell <= 80:
        water_as_int -= value_of_cell
        total_effort += value_of_cell * 0.25
        total_fire += value_of_cell
        list_with_cells.append(value_of_cell)

    elif type_of_fire == "Low" and 1 <= value_of_cell <= 50:
        water_as_int -= value_of_cell
        total_effort += value_of_cell * 0.25
        total_fire += value_of_cell
        list_with_cells.append(value_of_cell)

print("Cells:")
for num in list_with_cells:
    print(f" - {num}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")