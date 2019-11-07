while True:

    a = 0
    b = []

    j = input("Enter a number > ")

    if j == "exit":
        break
    else:

        i = int(j)

        if i == 1:
            print("1 is unitary\n")
        elif i == 0:
            print("0 is composite with infinitely many factors.\n")
        elif i < 0:
            print("Please enter a positive number.\n")
        elif i < 10000000:
            for x in range(1,i+1):
                if i%x == 0:
                    a += 1
                    b.append(x)
            if a == 2:
                print(f"{i} is prime \n")
            else:
                print(f"{i} is composite with {a} factors: {b} \n")
        else:
            if i%2 == 0:
                print(f"{i} is composite, 2 is a factor.\n")
            elif i%3 == 0:
                print(f"{i} is composite, 3 is a factor.\n")
            elif i%5 == 0:
                print(f"{i} is composite, 5 is a factor.\n")
            else:
                y = 7
                while y < 100000000:
                    if i%y == 0 and i != y:
                        print(f"{i} is composite, {y} is a factor.\n")
                        break
                    if i == y:
                        print(f"{i} is prime.\n")
                        break
                    if y == 99999999:
                        print("Operation overrun.\n")
                        break
                    else:
                        y += 2
