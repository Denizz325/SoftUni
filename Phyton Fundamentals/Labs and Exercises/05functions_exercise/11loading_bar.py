def loading_bar(sum_number) -> str:
    if sum_number == 100:
        return "100% Complete\n[%%%%%%%%%%]"
    loaded_percent = sum_number // 10
    return f"{sum_number}% [{'%' * loaded_percent}{'.' * (10 - loaded_percent)}]\nStill loading..."




number = int(input())

print(loading_bar(number))