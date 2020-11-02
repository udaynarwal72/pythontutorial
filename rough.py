a1=int(input("a: "))
b2=int(input("b: "))

def function(a,b):
    """
    This is function for finding average
    """
    average=(a+b)/2
    return average
c = function(a1,b2)
print(c)
print(function.__doc__)