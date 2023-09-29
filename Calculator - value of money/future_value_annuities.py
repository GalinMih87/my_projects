# Въвеждане на началния депозит, годишната лихва и периода
initial_deposit = float(input("Въведете начален депозит: "))
annual_interest = float(input("Въведете годишна лихва (%): "))
period = int(input("Въведете периода (години): "))

# Изчисление на бъдещата стойност на анюитета
annuities = ((1 + annual_interest / 100) ** period - 1) / (annual_interest / 100)
future_value = initial_deposit * annuities

# Извеждане на резултата
print(f"Бъдещата стойност на вашия депозит след {period} години ще бъде: {future_value:.2f}")
print(f"Aнюитета е равен на: {annuities:.4f}")