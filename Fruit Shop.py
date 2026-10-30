
# https://github.com/USERNAME/REPOSITORY

def analyze_shopping_list(**kwargs):
    fruits_count = len(kwargs)
    total_cost = sum(kwargs.values())

    most_expensive = max(kwargs, key=kwargs.get)
    cheapest = min(kwargs, key=kwargs.get)

    print(f"You have {fruits_count} fruits in your shopping list")
    print(f"The total cost of the shopping list is {total_cost}")
    print(f"The most expensive fruit is {most_expensive} with the price of {kwargs[most_expensive]}")
    print(f"The cheapest fruit is {cheapest} with the price of {kwargs[cheapest]}")


fruits = {}

while True:
    user_input = input()

    if user_input == "finish":
        break

    name, price = user_input.split()
    fruits[name] = int(price)

analyze_shopping_list(**fruits)

