#БСБО-05-19 Салынь Даниил Леонидович
def letters_to_numbers(line: str):
    line = line.replace("A", "1")
    line = line.replace("B", "2")
    line = line.replace("C", "3")
    line = line.replace("D", "4")
    line = line.replace("E", "5")
    line = line.replace("F", "6")
    line = line.replace("G", "7")
    line = line.replace("H", "8")
    return line


def numbers_to_letters(line: str):
    line = line[:1].replace("1", "A") + line[1:]
    line = line[:1].replace("2", "B") + line[1:]
    line = line[:1].replace("3", "C") + line[1:]
    line = line[:1].replace("4", "D") + line[1:]
    line = line[:1].replace("5", "E") + line[1:]
    line = line[:1].replace("6", "F") + line[1:]
    line = line[:1].replace("7", "G") + line[1:]
    line = line[:1].replace("8", "H") + line[1:]
    return line


def coords_to_cell(x: int, y: int):
    return str(x) + str(y)


def possible_turns(cell: str):
    cell = letters_to_numbers(cell)
    first_coordinate = int(cell[:1])
    second_coordinate = int(cell[1:])
    if first_coordinate + 2 < 9:
        if second_coordinate + 1 < 9:
            print(numbers_to_letters(coords_to_cell(first_coordinate + 2, second_coordinate + 1)))
        if second_coordinate - 1 > 0:
            print(numbers_to_letters(coords_to_cell(first_coordinate + 2, second_coordinate - 1)))
    if first_coordinate - 2 > 0:
        if second_coordinate + 1 < 9:
            print(numbers_to_letters(coords_to_cell(first_coordinate - 2, second_coordinate + 1)))
        if second_coordinate - 1 > 0:
            print(numbers_to_letters(coords_to_cell(first_coordinate - 2, second_coordinate - 1)))
    if second_coordinate + 2 < 9:
        if first_coordinate + 1 < 9:
            print(numbers_to_letters(coords_to_cell(first_coordinate + 1, second_coordinate + 2)))
        if first_coordinate - 1 < 9:
            print(numbers_to_letters(coords_to_cell(first_coordinate - 1, second_coordinate + 2)))
    if second_coordinate - 2 < 9:
        if first_coordinate + 1 < 9:
            print(numbers_to_letters(coords_to_cell(first_coordinate + 1, second_coordinate - 2)))
        if first_coordinate - 1 < 9:
            print(numbers_to_letters(coords_to_cell(first_coordinate - 1, second_coordinate - 2)))


possible_turns(input())
