# Въвеждане на бъдещата стойност, годишната лихва и периода
future_value = float(input("Въведете бъдещата стойност: "))
annual_interest = float(input("Въведете годишна лихва (%): "))
period = int(input("Въведете периода (години): "))

# Изчисление на настоящата стойност на бъдещия доход
present_value = future_value / (1 + annual_interest / 100)**period

# Извеждане на резултата
print(f"Наcтоящата стойност на бъдещия доход е: {present_value:.2f}")