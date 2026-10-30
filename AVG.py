# https://github.com/Hamedpgm31/python-AIM-Bootcamp-projects

def average(numbers):
    return sum(numbers) / len(numbers)


while True:
    try:
        numbers = list(map(float, input().split()))

        if len(numbers) == 0:
            raise ValueError

        print(f"{average(numbers):.2f}")
        break

    except ValueError:
        print("Invalid Input! Enter a valid input.")