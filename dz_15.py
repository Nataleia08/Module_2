result = None
operand = None  # число
operator = None  # операція
wait_for_number = True

while True:
    if wait_for_number:
        try:
            operand = int(input())
        except ValueError:
            print("is not a number. Try again")
        else:
            if operator == "+":
                result = result + operand
            elif operator == "-":
                result = result - operand
            elif operator == "*":
                result = result * operand
            elif operator == "/":
                result = result / operand
            elif operator == None:
                result = operand
            wait_for_number = False
    else:
        operator = input()
        if (operator == "="):
            break
        elif (operator == "+") or (operator == "-") or (operator == "/") or (operator == "*"):
            wait_for_number = True
        else:
            print("is not '+' or '-' or '/' or '*'. Try again")
            continue
print(result)
