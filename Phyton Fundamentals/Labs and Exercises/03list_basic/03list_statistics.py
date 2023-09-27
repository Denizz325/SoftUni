num_of_lines = int(input())

positive_list = []
negative_list = []
count = 0

for i in range(num_of_lines):
    num = int(input())

    if num >= 0:
        positive_list.append(num)
    else:
        negative_list.append(num)


print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}\nSum of negatives: {sum(negative_list)}")

# За да не правя няколко принта мога да преместя израз на долния ред с помоща на \n




