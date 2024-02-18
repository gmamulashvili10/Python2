# TODO
from cs50 import get_float

while True:
    dollars = get_float("Change owed: ")
    if dollars >= 0:
        break

cents = round(dollars * 100)
coins = 0  # 1 2 3
denominations = [25, 10, 5, 1]

for denom in denominations:
    coins += cents // denom
    cents %= denom  # a %= b | a = a % b

print(coins)