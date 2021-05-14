# БСБО-05-19 Салынь Даниил Леонидович
import random

ascii_lowercase = 'abcdefghijklmnpqrstuvwxyz23456789'


def generate_password(m):
    password = generate_ch_password(m)
    return password


def generate_ch_password(m):
    res_password = ""
    while len(res_password) < m:
        if (ch := ascii_lowercase[
            random.randint(0, len(ascii_lowercase) - 1)]) not in res_password and ch.upper() not in res_password:
            ch.lower()
            if ch in ["i", "l"]:
                case = 0
            else:
                case = random.randint(0, 1)
            if case == 0:
                res_password += ch
            else:
                res_password += ch.upper()
    return res_password


def main(n, m):
    return [generate_password(m) for _ in range(n)]


print('Случайный пароль из 7 символов:', generate_password(7))
print('10 случайных паролей длиной 15 символов:')
print(*main(10, 15), sep='\n')
