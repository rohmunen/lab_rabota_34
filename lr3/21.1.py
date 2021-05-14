#БСБО-05-19 Салынь Даниил Леонидович
def from_string_to_list(string: str, container: list):
    list_string = string.split(sep=" ")
    for i in range(len(list_string)):
        container.append(list_string[i])


a = [1, 2, 3]
from_string_to_list("1 3 99 52", a)
print(*a)
a = [77, 'abc']
from_string_to_list("", a)
print(*a)