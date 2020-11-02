a = input("Enter the name of the file: ")
def function(b):
    """
    This is a function for taking input from the file
    """
    f = open(b)
    content = f.read()
    f.close()
    return content
c = function(a)
print(c)
