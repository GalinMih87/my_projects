import random
from simple_colors import *

zodiac = ""
list = [1, 2, 3, 4, 5, 6]

def print_header():
    print("**********************************************************")
print_header()

print(red("Ако желаете да излезете от програмата, моля напишете Край"))
print_header()
print()
while True:
    zodiac = input(cyan("Моля въведете зодия, като започнете с главна буква:", ["underlined"]))
    print()
    if zodiac == "Край":
        break

    if zodiac == "Овен" or zodiac == "Телец" or zodiac == "Близнаци" or zodiac == "Рак" or zodiac == "Лъв" \
    or zodiac == "Дева" or zodiac == "Везни" or zodiac == "Скорпион" or zodiac == "Стрелец" or zodiac == "Козирог" \
    or zodiac == "Водолей" or zodiac == "Риби":
        print(green("Късмет: ", ["bold", "underlined", "italic"]), end="")
        print(random.choice(list) * "\N{four leaf clover}") # късмет U+1F340 - четирилисна детелина (four leaf clover)
        print(cyan("Здраве: ", ["bold", "underlined", "italic"]), end="")
        print(random.choice(list) * "\N{coffin}") # здраве U+26B0 - ковчег (coffin)
        print(red("Любов: ", ["bold", "underlined", "italic"]), end="")
        print(random.choice(list) * "\N{heart with arrow}") # любов U+1F498 - сърце (heart with arrow)
        print(yellow("Щастие: ", ["bold", "underlined", "italic"]), end="")
        print(random.choice(list) * "\N{clinking beer mugs}") # щастие U+1F37B - две бири (clinking beer mugs)
        print(blue("Пари: ", ["bold", "underlined", "italic"]), end="")
        print(random.choice(list) * "\N{money bag}") # пари U+1F4B0 - торба с пари (money bag)
        print(magenta("Работа: ", ["bold", "underlined", "italic"]), end="")
        print(random.choice(list) * "\N{brain}") # работа U+1F9E0	- хакер (brain)
        print()
    else:
        print("Въвели сте грешна зодия!")
