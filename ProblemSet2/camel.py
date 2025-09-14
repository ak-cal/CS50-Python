def main():
    camelCase = input("camelCase: ")
    snake = ""
    for i in camelCase:
        if i.isupper():
            snake = snake + "_" + i.lower()
        else:
            snake += i
    print(snake)

 
main()