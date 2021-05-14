#БСБО-05-19 Салынь Даниил Леонидович
lastTicket = ""


def lucky_ticket(ticket: int):
    one_sum = 0
    two_sum = 0
    one_ticket = list(str(ticket)[:3])
    two_ticket = list(str(ticket)[3:])
    for i in range(3):
        one_sum += int(one_ticket[i])
        two_sum += int(two_ticket[i])
    if one_sum == two_sum:
        return True
    else:
        return False


def lucky(ticket: int):
    global lastTicket
    if lucky_ticket(lastTicket) and lucky_ticket(ticket):
        print("Счастливый")
    else:
        print("Несчастливый")


lastTicket = int(input())
lucky(int(input()))
