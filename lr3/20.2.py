#БСБО-05-19 Салынь Даниил Леонидович
global_name = ""
global_vacationDates = ""


def setup_profile(name, vacationDates):
    global global_name
    global global_vacationDates
    global_name = name
    global_vacationDates = vacationDates


def print_application_for_leave():
    print("Заявление на отпуск в период " + global_vacationDates + ". " + global_name)


def print_holiday_money_claim(amount: str):
    print(
        "Прошу выплатить " + amount + " отпускных денег. " + global_name + " На время отпуска в период " + global_vacationDates)


def print_attorney_letter(toWhom: str):
    print("Моим заместителем " + toWhom + ". ", end="")
    print(global_name)


setup_profile("Иван Петров", "1 июня - 20 июня")
print_application_for_leave()
print_holiday_money_claim("15 тысяч пиастров")
print_attorney_letter("Василий Васильев")
