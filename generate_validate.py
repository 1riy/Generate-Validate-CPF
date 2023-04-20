import random
import sys
import re

def title():
        tit = 'CPF GENERATOR'
        tup = '-=' * len(tit)
        aup = len(tup)
        print(tup)
        print(f'{tit: ^{aup}}')
        print('-=' * len(tit))


def generatecpf():
    amount = int(input("\nQuantos? "))
    for i in range(amount):
        nine_digits = ''
        for c in range(9):
            nine_digits += str(random.randint(0, 9))

        regres_count = 10
        sum = 0
        for digit in nine_digits:
            sum += int(digit) * regres_count
            regres_count -= 1

        first_digit = (sum * 10) % 11
        first_digit = first_digit if first_digit <= 9 else 0

        ten_digits = nine_digits + str(first_digit)
        regres_11count = 11
        sum2 = 0

        for digit in ten_digits:
            sum2 += int(digit) * regres_11count
            regres_11count -= 1

        second_digit = (sum2 * 10) % 11
        second_digit = second_digit if second_digit <= 9 else 0

        randomcpf = f'{nine_digits}{first_digit}{second_digit}'
        print(randomcpf)


def verifycpf():
    verify_cpf = str(input('Validar: '))
    verify_cpf = re.sub(
        r'[^0-9]',
        '',
        verify_cpf
    )

    if verify_cpf == verify_cpf[0] * len(verify_cpf):
        print("CPF inválido.")
        sys.exit()

    nine_digits = verify_cpf[:9]
    regres_count = 10
    sum = 0

    for digit in nine_digits:
        sum += int(digit) * regres_count
        regres_count -= 1

    first_digit = (sum * 10) % 11
    first_digit = first_digit if first_digit <= 9 else 0

    ten_digits = nine_digits + str(first_digit)
    regres_11count = 11
    sum2 = 0

    for digit in ten_digits:
        sum2 += int(digit) * regres_11count
        regres_11count -= 1

    second_digit = (sum2 * 10) % 11
    second_digit = second_digit if second_digit <= 9 else 0

    validatedcpf = f'{nine_digits}{first_digit}{second_digit}'

    if verify_cpf == validatedcpf:
        print('CPF válido.')
    else:
        print('CPF inválido.')


def verify():
    verify2 = input("O que deseja fazer?\n[GERAR]\n[VALIDAR]\n- ").lower()

    if verify2 == 'gerar':
        generatecpf()
        sys.exit()
    elif verify2 == 'validar':
        verifycpf()
        sys.exit()
    else:
        verify()

    return verify2


title()
verify()

