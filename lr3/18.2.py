#БСБО-05-19 Салынь Даниил Леонидович
def ask_password():
    flag = False
    for i in range(3):
        if input() == "password":
            flag = True
            print("Пароль принят")
            break
    if not flag:
        print("В доступе отказано")


ask_password()

