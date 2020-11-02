rows = int(input("Enter the no. of rows: "))
b = bool(int(input("Enter the no.1 or 0: ")))

if b == True:
    for n in range(rows+1):
        print("*" * n)
else:
    for k in range(rows, 0, -1):
        print("*" * k)
