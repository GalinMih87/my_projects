# Въвеждане на периодично плащане, годишната лихва и периода
cash_flow = float(input("Въведете периодично плащане: "))
annual_interest = float(input("Въведете годишна лихва (%): "))
period = int(input("Въведете периода (години): "))

# Преобразуване на годишната лихва в десетичен вид
interest_rate = annual_interest / 100

# Изчисление на броя на периодичните плащания
total_payments = period

# Изчисление на настоящата стойност на анюитета
present_value = 0
for i in range(1, total_payments + 1):
    present_value += cash_flow / ((1 + interest_rate) ** i)

# Извеждане на резултата
print(f"Наcтоящата стойност на {period} плащания по {cash_flow:.0f} за период от {period} години ще бъде: {present_value:.2f}")
