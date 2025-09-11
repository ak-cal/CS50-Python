def main():
    phrase = input("Type a phrase/sentence: ")
    playback(phrase)

def playback(phrase):
    phrase = phrase.replace(" ", "...")
    print(phrase)

main()