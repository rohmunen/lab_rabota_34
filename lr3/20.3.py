#БСБО-05-19 Салынь Даниил Леонидович
old_jokes = ""


def print_only_new(joke: str):
    global old_jokes
    if joke not in old_jokes:
        print(joke)
        old_jokes += joke


while True:
    print_only_new(input())
