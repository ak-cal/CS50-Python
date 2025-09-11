def main():
    mass = int(input("Enter Mass: "))
    einstein(mass)

def einstein(m):
    c = 300000000
    E = m*c**2
    print(E)

main()  