rows = int(input("Enter the no. of rows: "))
b= bool(input("Enter the no.1 or 0: "))
# b=bool(c)

if b == True:
    for n in range(rows+1):
        print("*" * n)
else:
    for k in range(rows, 0, -1):
        print("*" * k)

# no_of_lines = int(input("Enter number of lines : "))
# patt= int((input ("Enter 1 to print incremental pattern or 0 to print inverted pattern: ")))
# pattern = bool(patt)
# if pattern == True:
#     for n in range(no_of_lines+1):
#         print( "* " * n )
# else:
#     for m in range(no_of_lines, 0, -1):
#         # print(n)
#         print( "* " * m )
