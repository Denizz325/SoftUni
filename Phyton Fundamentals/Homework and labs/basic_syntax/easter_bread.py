budget = float(input())

flour = float(input())
eggs = flour * 0.75
milk = flour * 1.25

colored_eggs = 0
number_of_loaves = 0
milk_in_ml = 1000

coast_per_loave = (flour + eggs + (milk / 4))

while budget >= coast_per_loave:
    budget -= (flour + eggs + (milk / 4))
    number_of_loaves += 1
    colored_eggs += 3

    if number_of_loaves % 3 == 0:
        lost_eggs = number_of_loaves - 2
        colored_eggs -= lost_eggs

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")




