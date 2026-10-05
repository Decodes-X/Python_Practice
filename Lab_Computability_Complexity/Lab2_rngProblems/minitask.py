import random
List = []
for i in range(1,100):
    List.append(i)


def Check(first,last):
    TwoReturn = []
    checker = 0
    outvalue = last
    while first > outvalue:
        outvalue = checker * last
        if outvalue > first:
            rvalue = last * (checker - 1)
            out = Addition(rvalue,first)
            TwoReturn.append(last)
            TwoReturn.append(out)
        elif outvalue == first:
            TwoReturn.append(0)
            TwoReturn.append(last)
        else:
            checker += 1
    else:
        return TwoReturn


def Addition(remd,value):
    return value - remd

def GetVal():
    a = random.randrange(0, len(List))
    b = random.randrange(0, len(List))
    c = ""
    d = ""
    if b > a:
        d = a
        c = b
        return c,d
    return a,b

def GCD():
    a, b = GetVal()
    OValues = [a,b]
    NewVal = [a,b]
    while NewVal[0] > 0:
        if NewVal[0] < 0 :
            return "Could not compute"
        NewVal = Check(NewVal[0],NewVal[1])
    else:
        return NewVal,OValues


def main():
    fev = GCD()
    print(
        fev[1][0],"\n",
        fev[1][1],"\n",
        "GCD of the two: ",fev[0][1],"\n")

if __name__ == "__main__":
    main()
