first_number = 0
second_number = 0
result = 0
next_operation = True
continue_op = True
add = lambda a,b:a+b
subtract = lambda a,b:a-b

def multiply(a,b):
    """ takes two numbers as input and returns their product"""
    return a*b

def divide(a,b):
    """takes two numbers and returns division of them"""
    if b == 0:
        print("Invalid operation")
        return 0
    else:
        return a/b
    
operation = {
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply
}

    
while next_operation:
    continue_op = True
    first_number = int(input("Enter your first number: "))
    while continue_op:
        for op in operation:
            print(op)
        operator = input("Select your operator: ")
        second_number = int(input("Enter your second number: "))
        result = operation[operator](first_number,second_number)
        print(f"The result is: {result}")
        continue_op = True if input("Do you want to continue from here y/n? ").strip().lower()[0]=="y" else False
        first_number = result