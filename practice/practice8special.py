def getdate():
    import datetime
    return datetime.datetime.now()



date = str(getdate())


id1 = input("Enter your name")
pass1 = input("Enter your pass")


n = id1+".txt"


def take(b):
    if (b == 1):
        if (c == 1):
            value = input("Enter for exercise: ")
            with open(n, "a") as op:
                print(op.write(date + " " + value))
        elif (c == 2):
            value = input("Enter for diet: ")
            with open(n, "a") as op:
                print(op.write(date+" "+value))
    elif (b == 2):
        if (c == 1):
            value = input("Enter for exercise: ")
            with open(n, "a") as op:
                print(op.write(date + " " + value))
        elif (c == 1):
            value = input("Enter for diet: ")
            with open(n, "a") as op:
                print(op.write(date+" "+value))

    elif (b == 3):
        if (c == 1):
            value = input("Enter for exercise: ")
            with open(n, "a") as op:
                print(op.write(date + " " + value))
        elif (c == 2):
            value = input("Enter for diet: ")
            with open(n, "a") as op:
                print(op.write(date+" "+value))




def retrive(b):
    if (b == 1):
        if (c == 1):
            with open(n) as op:
                for i in op:
                    print(i)
        elif (c == 2):
            with open(n) as op:
                for i in op:
                    print(i)
    if (b == 2):
        if (c == 1):
            with open(n) as op:
                for i in op:
                    print(i)
        elif (c == 2):
            with open(n) as op:
                for i in op:
                    print(i)
    if (b == 3):
        if (c == 1):
            with open(n) as op:
                for i in op:
                    print(i)
        elif (c == 2):
            with open(n) as op:
                for i in op:
                    print(i)



a = int(input("""Enter 
               (1) for log 
               (2) for retrive\n
               """))
k = int(input("""Enter
              (1) for harry
              (2) for rohan
              (3) for hammed\n
              """))
c = int(input("""Enter 
            (1) for Exercise 
            (2) for diet\n
            """))



if a == 1:
    take(k)
elif a == 2:
    retrive(k)