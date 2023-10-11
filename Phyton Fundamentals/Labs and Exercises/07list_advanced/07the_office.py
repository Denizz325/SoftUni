def check_employ_happiness():
    happiness_list = list(map(int, input().split()))
    happiness_factor = int(input())

    improve_happiness = [happiness * happiness_factor for happiness in happiness_factor]
    average_happiness = sum(improve_happiness) / len(improve_happiness)

    happy_count = sum(happiness >= average_happiness for happiness in improve_happiness)
    total_count = len(improve_happiness)

    message = "happy" if tot
print(f"Score: {happy_count}/{total_count}. Employees are happy!")