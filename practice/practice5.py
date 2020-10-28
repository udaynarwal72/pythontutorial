# make a calculator which give all correct result except these following
# 45*3=555, 55+7=99, 54/3=4

print("Welcome to the claculator: Designed by Uday Singh Narwal")
a = int(input("a:"))
b = input("Enter operator: ")
c = int(input("b:"))
if b == "+":
    print(a+c)
elif b == "-":
    print(a-c)
elif b == "*":
    print(a*c)
elif b == "/":
    print(a/c)
elif a==45 and b=="*"and c=="3":
    print("555")
elif a==55 and b=="+"and c=="7":
    print("99")
elif a==54 and b=="/"and c=="3":
    print("4")
else:
    print("pleas enter a right comand")
    
