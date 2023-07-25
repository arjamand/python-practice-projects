
def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return round(n1/n2,3)

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
    }


def calculator():

    num1=float(input("1st number : "))


    for x in operations:
        print(x)

    op=input("Choose an operation from above ! \n>>> ")
    num2=int(input("2nd number : "))
    function=operations[op]
    answer_=function(num1,num2)
    print(f"{num1} {op} {num2} = {answer_}")

    option=input("Would you like to continue calculation with the answer (yes , no): ")

    signal=True
    while signal==True:
        for x in operations:
            print(x)
        op=input("Choose an operation from above ! \n>>> ")
        num3=float(input(f"Next number : "))
        function=operations[op]
        answer_=function(answer_,num3)
        print(f"{answer_} {op} {num3} = {answer_}")
        option=input(f"Would you like to continue calculation with the answer({answer_}) (yes , no),start a new clculation (new): ")
        if option=="no":
            signal==False
        elif option=="new":
            calculator()

calculator()           