# БСБО-05-19 Салынь Даниил Леонидович
ru_alphabet = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
ru_upper_alphabet = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")


def encrypt_caesar(msg: str, shift=3):
    global ru_alphabet
    global ru_upper_alphabet
    list_msg = list(msg)
    for i in range(len(list_msg)):
        if list_msg[i] in ru_alphabet:
            list_msg[i] = ru_alphabet[(ru_alphabet.index(list_msg[i]) + shift) % 33]
        elif list_msg[i] in ru_upper_alphabet:
            list_msg[i] = ru_upper_alphabet[(ru_upper_alphabet.index(list_msg[i]) + shift) % 33]
    return "".join(list_msg)


def decrypt_caesar(msg: str, shift: int):
    global ru_alphabet
    global ru_upper_alphabet
    list_msg = list(msg)
    for i in range(len(list_msg)):
        if list_msg[i] in ru_alphabet:
            list_msg[i] = ru_alphabet[abs(ru_alphabet.index(list_msg[i]) - shift) % 33]
        elif list_msg[i] in ru_upper_alphabet:
            list_msg[i] = ru_upper_alphabet[abs(ru_upper_alphabet.index(list_msg[i]) - shift) % 33]
    return "".join(list_msg)


msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)
