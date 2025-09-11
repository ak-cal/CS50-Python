def main():
    time = convert(input("What time is it? "))
    if (time >= 7 and time <= 8):
        print("Breakfast Time")
    elif (time >= 12 and time <= 13):
        print("Lunch Time")
    elif (time >= 18 and time <= 19):
        print("Dinner Time")


def convert(time):
    hours, minutes = time.split(":")
    minutes =int(minutes)
    hours = int(hours)
    return hours + (minutes / 60)

if __name__ == "__main__":
    main()