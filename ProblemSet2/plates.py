"""
“done All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters. done
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
"""

def main():
    # plate = input("Plate: ")
    plate = "C1"
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
 
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    if (s.isalnum() == False):
        return False
    

    number_found = False
    for i in range(len(s)):
        ch = s[i]
        if ch.isdigit():
            if ch=='0' and number_found:
                return False
            number_found == True
        else:
            if number_found:
                return True

    return True
    
main()