# https://github.com/Hamedpgm31/python-AIM-Bootcamp-projects

def fruit_analysis(**kwargs):
    count = len(kwargs)
    total = sum(kwargs.values())

    expensive = max(kwargs, key=kwargs.get)
    cheapest = min(kwargs, key=kwargs.get)

    print(f"You have {count} fruits in your shopping list...")
    print(f"The total cost of the shopping list is {total}")
    print(f"the most expensive fruit is {expensive} with the price of {kwargs[expensive]}")
    print(f"The cheapest fruit is {cheapest} with the price of {kwargs[cheapest]}")


fruits = {}

while True:
    data = input().split()

    if data[0] == "finish":
        break

    fruits[data[0]] = int(data[1])

fruit_analysis(**fruits)