def main():
    text = input("Input: ").casefold()
    outputText = ""

    
    for i in text:
        if i in ['a', 'e', 'i', 'o', 'u']:
            text = text.replace(i, "")
        else:
            outputText += i

    print(outputText)

main()

#GPT CODE
"""
def main():
    text = input("Input: ")
    output = ""

    for char in text:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            output += char

    print(output)


if __name__ == "__main__":
    main()
"""
