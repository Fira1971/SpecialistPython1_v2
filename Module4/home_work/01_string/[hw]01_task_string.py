# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

string1 = input("Введите строку с точками и запятыми: ")

new_sting1 = string1.count('.')
new_sting2 = string1.count(',')
if new_sting1 > new_sting2:
    print("Точек в строке больше, чем запятых")
elif new_sting1 < new_sting2:
    print("Запятых в строке больше, чем точек")
else:
    print("Точек и запятых в строке поровну")
