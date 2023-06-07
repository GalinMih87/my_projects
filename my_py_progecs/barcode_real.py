from barcode import EAN13
number1 = 'Bate Galio e pich'
number2 = '3801234123457'
my_code1 = EAN13(number1)
my_code2 = EAN13(number2)
my_code1.save("new1_code")
my_code2.save("new2_code")