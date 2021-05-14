#БСБО-05-19 Салынь Даниил Леонидович
def bracket_check(test_string):
    opening_brackets_count = 0
    closing_brackets_count = 0
    test_list = list(test_string)
    for i in range(len(test_list)):
        if test_list[i] == "(":
            opening_brackets_count = opening_brackets_count + 1
        elif test_list[i] == ")":
            closing_brackets_count = closing_brackets_count + 1
    if closing_brackets_count != opening_brackets_count:
        print("NO")
    else:
        print("YES")


bracket_check(input())
