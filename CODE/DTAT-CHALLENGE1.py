#O ano que pode ser dividido por 4, é um ano bissexto, a menos que:
#O ano pode ser dividido por 100, então NÃO é um ano bissexto, a menos que:
#O ano também é divisível por 400. Então é um ano bissexto.

def calc_resto(year,qtd):
    result = year % qtd
    return result

def is_leap(year):
    leap = False
    if calc_resto(year,4) == 0:
        if ((calc_resto(year,100)) == 0 and (calc_resto(year,400) == 0)):
            leap = True
        else:
            leap = False
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))
