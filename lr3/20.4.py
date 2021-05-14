#БСБО-05-19 Салынь Даниил Леонидович
base = ["Иван", "Юлия Иванкова"]
def hello(name):
    print("Здравствуйте, " + name + "! Вашу карту ищут...")


def search_card(name):
    global base
    if name in base:
        print("Ваша карта с номером " + str(base.index(name) + 1) + " найдена")
    else:
        print("Ваша карта не найдена")


hello("Иван")
search_card("Иван")
hello("Юлия Иванова")
search_card("Юлия Иванова")