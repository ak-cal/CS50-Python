def main():
    emoticon = input("Enter a text-based emoji: ")
    emoticon = convert(emoticon)

    print(emoticon)

def convert(emoji):
    emoji_dict = {
        ":)": "🙂",
        ":(": "🙁"
    }
    for word, emoticon in emoji_dict.items():
        emoji = emoji.replace(word, emoticon)
    return emoji

main()