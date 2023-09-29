# Въвеждане на началния депозит, годишната лихва и периода
initial_deposit = float(input("Въведете начален депозит: "))
annual_interest = float(input("Въведете годишна лихва (%): "))
period = int(input("Въведете периода (години): "))

# Изчисление на бъдещата стойност
return_on_investment = (1 + (annual_interest / 100)) ** period
future_value = initial_deposit * return_on_investment

# Извеждане на резултата
print(f"Бъдещата стойност на вашия депозит след {period} години ще бъде: {future_value:.2f}")
print(f"Доходa от инвестицията e в размер на: {future_value - initial_deposit:.2f}")