# БСБО-05-19 Салынь Даниил Леонидович
def comments_list(string: str):
    string = string.replace("\'\n\'", "СЛЕШЕН")
    line_count = 0
    while "\n" in string:
        line_count += 1
        substr = string[:string.index("\n")]
        if substr.find("#") > -1:
            comment = substr[substr.index("#"):]
            print("Line " + str(line_count) + ": " + comment.replace("СЛЕШЕН", "\'\\n\'"))
            string = string[string.index("\n") + 1:]
        else:
            string = string[string.index("\n") + 1:]


comments_list(
    "import sys\nfor line in sys.stdin:\n# rstrip('\n') \"отрезает\" от строки line,\n# идующий справа символ перевода строки,\n # ведь print сам переводит строку\nprint(line.rstrip('\n'))")
