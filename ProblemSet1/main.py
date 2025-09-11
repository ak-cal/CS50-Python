import re 

def main():
    choice = input("What would you like to do? " \
    "\n1. Deep Thought" \
    "\n2. Home Federal Savings Bank" \
    "\n3. File Extensions" \
    "\n4. Math Interpreter" \
    "\n5. Meal Time" \
    "\nChoice: ")

    match choice:
        case "1":        
            answer = input("What is the Answer to the Great Question of Life, the Univeerse and Everything? ")
            if (answer == "42") | (answer == "forty-two"):
                print("Yes")
            else:
                print("Wrong Answer")
        case "2":
            greet = input("Greeting: ")
            answer = bankchecker(greet)
            print(answer)
        case "3":
            filetype = filechecker(input("File Name: "))
            print(filetype)
        case "4":
            exp = input("Expression: ")
            interpret(exp)
          
        case "5":
            time = convert(input("What time is it? "))
            if (time >= 7 and time <= 8):
                print("Breakfast Time")
            elif (time >= 12 and time <= 13):
                print("Lunch Time")
            elif (time >= 18 and time <= 19):
                print("Dinner Time")


def bankchecker(greet):  
    g = greet.rstrip().casefold()
    if re.match(r"^hello\b", g):
        return "$0"
    elif g.casefold().startswith("h"):
        return "$20"
    else:
        return "$100"
    
def filechecker(fn):
    fn = fn.strip().casefold()

    if ("." not in fn):
        return "application/octet-stream"

    fn, ext = fn.rsplit(".", 1)
    ext_dict = {
        "jpeg": "image/jpeg",
        "jpg": "image/jpeg",
        "png": "image/png",
        "gif": "image/gif",
        "txt": "text/txt",
        "pdf": "text/pdf",
        "zip": "file/zip"
    }

    return ext_dict.get(ext, "application/octet-stream")

def interpret(exp):
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

def convert(time):
    hours, minutes = time.split(":")
    minutes =int(minutes)
    hours = int(hours)
    return hours + (minutes / 60)


main()
