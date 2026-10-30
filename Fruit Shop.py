# https://github.com/Hamedpgm31/python-AIM-Bootcamp-projects

def fruit_analysis(**kwargs):
    count = 0
    total = 0

    for fruit in kwargs:
        count += 1
        total += kwargs[fruit]

    expensive = max(kwargs, key=kwargs.get)
    cheapest = min(kwargs, key=kwargs.get)

    print(count)
    print(total)
    print(expensive)
    print(cheapest)


fruits = {}

while True:
    data = input().split()

    if data[0] == "finish":
        break

    fruits[data[0]] = float(data[1])

fruit_analysis(**fruits)