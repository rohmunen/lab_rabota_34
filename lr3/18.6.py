#БСБО-05-19 Салынь Даниил Леонидович
def line(s: str, t: str):
    k = float(s[:s.find("x")])
    if s.find("+") > 0:
        b = float(s[s.find("+") + 1:])
    else:
        b = -1 * float(s[s.find("-") + 1:])
    if k * float(t[:t.find(";")]) + b == float(t[t.find(";") + 1:]):
        print("True")
    else:
        print("False")


line(input(), input())
