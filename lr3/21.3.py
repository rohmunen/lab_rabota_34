#БСБО-05-19 Салынь Даниил Леонидович
def swap(first, second):
    temp = []
    for i in range(len(second)):
        temp.append(second[i])
    second.clear()
    for i in range(len(first)):
        second.append(first[i])
    first.clear()
    for i in range(len(temp)):
        first.append(temp[i])


first = [1, 2, 3]
second = [4, 5, 6]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)
first = [1, 2, 3]
second = [4, 5, 6, 7]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)
