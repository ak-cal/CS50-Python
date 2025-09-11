import re

def main():
    greet = input("Greeting: ")
    answer = checker(greet)
    print(answer)

def checker(greet):  
    g = greet.rstrip().casefold()
    if re.match(r"^hello\b", g):
        return "$0"
    elif g.casefold().startswith("h"):
        return "$20"
    else:
        return "$100"
main()