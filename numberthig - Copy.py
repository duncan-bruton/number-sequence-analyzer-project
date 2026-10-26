import sys

elaina = True
fake = True

def fibonm():
    try:
        two = int(input("how many finbmic?: "))
    except ValueError:
        print("ENTER A NUMBER YOU CHUDDDD")
        
    three, four = 0, 1

    for i in range(two):
        print(f"{three} ", end="")
        three, four = four, three + four

def logan_paul():
    try:
        five = int(input("what number???: "))
    except ValueError:
        print("ENTER A NUMBER YOU CHUDDDD")
        return
    
    for i in range(2, five):
        if i < 2:
            continue

        if five % i == 0:
            return print("not prime :(")
        
    print(f"{five} is prime!!!")

def ksi():
    try:
        six = int(input("what range???: "))
    except ValueError:
        print("ENTER A NUMBER YOU CHUDDDD")
        return

    for i in range(1, six + 1):
        if i < 2:
            continue

        prime = True

        for j in range(2, i):
            if i % j == 0:
                prime = False
                break

        if prime:
            print(f"{i} ", end="")

def markiplier():
    try:
        seven = int(input("ughhh what number???: "))
    except ValueError:
        print("ENTER A NUMBER YOU CHUDDDD")
        return
    
    try:
        eight = int(input("ughhh how longg???: "))
    except ValueError:
        print("ENTER A NUMBER YOU CHUDDDD")
        return

    for i in range(1, eight + 1):
        print(f"{seven} x {i} = {seven * i}")

def factorio():
    try:
        nine = int(input("ughhh what number???: "))
    except ValueError:
        print("ENTER A NUMBER YOU CHUDDDD")
        return

    ten = []
    eleven = 0

    for i in range(1, nine):
        ten.append(nine - i)
        eleven = nine

    for i in range(len(ten) - 1):
        eleven *= ten[i]

    print(eleven)

def chudlatz():
    try:
        twelve = int(input("ughhh what positive number???: "))
    except ValueError:
        print("ENTER A NUMBER YOU CHUDDDD")
        return

    thirteen = 0

    while twelve != 1:
        if twelve % 2 == 0:
            twelve /= 2
            thirteen += 1
        else:
            twelve *= 3
            twelve += 1
            thirteen += 1
    print(f"it took {thirteen} steps to reach 1!!")

while elaina is fake:
    print("\n1. Fibonacci!!!")
    print("2. Check Prime!!!")
    print("3. Prime numbers in range!!!")
    print("4. MUltiplication table!!!")
    print("5. foctorial....")
    print("6. Collatz more like chuddd")
    print("7. END......")

    try:
        one = int(input("\nwhich one i ask?: "))
    except ValueError:
        print("ENTER A NUMBER 1 - 6 YOU CHUDDDD")
        continue

    if one == 1:
        fibonm()
    elif one == 2:
        logan_paul()
    elif one == 3:
        ksi()
    elif one == 4:
        markiplier()
    elif one == 5:
        factorio()
    elif one == 6:
        chudlatz()
    elif one == 7:
        for h in range(10000):
            for i in range(10000):
                for j in range(10000):
                    print("END END END END END END END END END END END END END END END END END END END END END END END END END END END END END END END END END END END END END END ")
            sys.exit()
        
        
