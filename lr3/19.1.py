#БСБО-05-19 Салынь Даниил Леонидович
def month_name(month_num: int, lang: str):
    if lang == "ru":
        if month_num == 1:
            print("Январь")
        elif month_num == 2:
            print("Февраль")
        elif month_num == 3:
            print("Март")
        elif month_num == 4:
            print("Апрель")
        elif month_num == 5:
            print("Май")
        elif month_num == 6:
            print("Июнь")
        elif month_num == 7:
            print("Июль")
        elif month_num == 8:
            print("Август")
        elif month_num == 9:
            print("Сентябрь")
        elif month_num == 10:
            print("Октябрь")
        elif month_num == 11:
            print("Ноябрь")
        elif month_num == 12:
            print("Декабрь")
    elif lang == "en":
        if month_num == 1:
            print("January")
        elif month_num == 2:
            print("February")
        elif month_num == 3:
            print("March")
        elif month_num == 4:
            print("April")
        elif month_num == 5:
            print("May")
        elif month_num == 6:
            print("June")
        elif month_num == 7:
            print("July")
        elif month_num == 8:
            print("August")
        elif month_num == 9:
            print("September")
        elif month_num == 10:
            print("October")
        elif month_num == 11:
            print("November")
        elif month_num == 12:
            print("December")


month_name(int(input()), input())
