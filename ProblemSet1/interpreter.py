def main():
    exp = input("Expression: ")
    operators = ["+", "-", "/", "*"]

    for op in operators:
        if op in exp:
            left, right = exp.split(op)
            left = float(left.strip())
            right = float(right.strip())

            ope = op
            break
    

    match ope:
        case "+":
            answer = left + right
        case "-":
            answer = left - right
        case "*":
            answer = left * right
        case "/":
            if right == 0:
                print("Cannot divide by Zero!")
            else:
                answer = left / right
        case _:
            print("invalid")
    print(answer)

main()