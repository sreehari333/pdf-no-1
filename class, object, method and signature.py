# 1) class,object,method and signature
#class
#example program for class

class MyClass:
    x = 5

#object
#example program for object
#create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)

#method
#example for methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hii my name is" + self.name)

p1 = person("sree hari", 21)
p1.myfunc()

#signature
#an example program for signature

def test(a, *, b):


   sig = signature(test)
   ba = sig.bind(10, b=20)
   test(*ba.args, **ba.kwargs)
