drink_number = int(input())
extra_number = int(input())
drink_name = input()
extra_name = input()
price_drink = 0

if drink_name == "coffee":
    price_drink = 1 * drink_number
    if extra_name == "sugar":
        price_drink += 0.40 * extra_number

elif drink_name == "tea":
    price_drink = 0.6 * drink_number
    if extra_name == "sugar":
        price_drink += 0.40 * extra_number

print(price_drink)