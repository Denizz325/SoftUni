product_info = input().split()
stock_dict = {}

for i in range(0, len(product_info), 2):
    food = product_info[i]
    quantity = product_info[i + 1]
    stock_dict[food] = int(quantity)

product_to_search = input().split()
for current_product in product_to_search:
    if current_product in stock_dict:
        print(f"We have {stock_dict[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")
