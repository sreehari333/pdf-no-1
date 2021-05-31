#global and local variables
#global variable

x = "sree"

def foo():
    print("x inside:", x)



foo()
print("x outside:", x)

#local variable

def foo():
    y = "sree"
    print(y)

foo()