def calculator(op,n1,n2):
    if op=="+":
        print(f"addition:{add(int(n1),int(n2))}")
    elif op=="-":
        print(f"subtraction:{subtraction(int(n1), int(n2))}")
    elif op=="*":
        print(f"multiplication:{multiply(int(n1), int(n2))}")
    elif op=="/":
        print(f"division:{division(int(n1), int(n2))}")


def add(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

calculator("+",9,3)
