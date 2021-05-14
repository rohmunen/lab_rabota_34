#БСБО-05-19 Салынь Даниил Леонидович
horses = []


def do_bet(number: int, bet: int):
    if number not in horses and bet > 0:
        print("Ваша ставка в размере " + str(bet) + " на лошадь " + str(number) + " принята")
        horses.append(number)
    else:
        print("Что-то пошло не так, попробуйте еще раз")


while True:
    do_bet(int(input()), int(input()))
