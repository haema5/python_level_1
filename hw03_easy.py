# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print()
print('Задание-1:')


def my_round(z2_digber, ndigits):
    z1_chk = 0

    z1_chk = str(z2_digber).split('.')[1]
    z1_chk = int(z1_chk[ndigits - 1])
    if z1_chk >= 5:
        z1_ost = float('0.' + '0' * (ndigits - 1) + '1')
        z2_digber = z2_digber + z1_ost

    z1_result = str(z2_digber).split('.')[0] + '.' + str(z2_digber).split('.')[1][:ndigits]
    return (z1_result)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print()
print('Задание-2:')


def lucky_ticket(lucky_ticket):
    z2_summ1 = 0
    z2_summ2 = 0

    z2_lt_len = len(str(lucky_ticket))
    if z2_lt_len % 2 == 0:
        z2_lt_len1 = z2_lt_len // 2
        z2_lt_len2 = z2_lt_len1
    else:
        z2_lt_len1 = z2_lt_len // 2
        z2_lt_len2 = z2_lt_len // 2 + 1

    z2_dig1 = str(lucky_ticket)[:z2_lt_len1]
    for z2_dig in z2_dig1:
        z2_summ1 += int(z2_dig)

    z2_dig2 = str(lucky_ticket)[z2_lt_len2:]
    for z2_dig in z2_dig2:
        z2_summ2 += int(z2_dig)

    if z2_summ1 == z2_summ2:
        return ('У Вас счастливый билет! (№ {})'.format(lucky_ticket))
    else:
        return ('У Вас обычный билет. (№ {})'.format(lucky_ticket))


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
