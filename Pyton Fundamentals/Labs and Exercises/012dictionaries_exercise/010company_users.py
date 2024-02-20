company_and_id = {}
command = input()
a = 0
while command != "End":
    company_name, employee_id = command.split(" -> ")

    if company_name not in company_and_id:
        company_and_id[company_name] = []
    if employee_id not in company_and_id[company_name]:
        company_and_id[company_name].append(employee_id)

    command = input()

for company_name, employee_id in company_and_id.items():
    id = " "
    print(f"{company_name}")
    for i in employee_id:
        id = i
        print(f"-- {id}")