def main():
    choice = input("What would you like to do? " \
    "\n1. Indoor.py" \
    "\n2. Playback Speed" \
    "\n3. Making Faces" \
    "\n4. Einstein" \
    "\n5. Tip Calculator" \
    "\nChoice: ")

    match choice:
        case "1":     
            indoor()
        case "2":
            phrase = input("Type a phrase/sentence: ")
            playback(phrase)
        case "3":
            emoticon = input("Enter a text-based emoji: ")
            emoticon = convert(emoticon)

            print(emoticon)
        case "4":
            mass = int(input("Enter Mass: "))
            einstein(mass)
        case "5":
            print("hello")


def indoor():
    to_lower = input("Type something in caps (HELLO): ").lower()
    print(to_lower)

def playback(phrase):
    phrase = phrase.replace(" ", "...")
    print(phrase)

def convert(emoji):
    emoji_dict = {
        ":)": "🙂",
        ":(": "🙁"
    }
    for word, emoticon in emoji_dict.items():
        emoji = emoji.replace(word, emoticon)
    return emoji

def einstein(m):
    c = 300000000
    E = m*c**2
    print(E)

def calculator():
    print("hello")
main()
