# When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.
class Base(object):
    # constructor
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

class Child(Base):
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age = age
    def getAge(self):
        self.age = age

class grandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self,name,age)
        self.address = address
    def getAddress(self):
        return self.address
objGrandChild = grandChild("Richard", 23, "Boston")
print("Name:", objGrandChild.name)
print("Age:", objGrandChild.age)
print("Address:", objGrandChild.address)

"""
Output:
Name: Richard
Age: 23
Address: Boston 
"""