# When a child class inherits from multiple parent classes, it is called Multiple Inheritance.

class Base1(object):
    # constructors
    def __init__(self):
        self.str1 = "USA"
        print("Base1 Class")
class Base2(object):
    # constructors
    def __init__(self):
        self.str2 = "Germany"
        print("Base2 Class")
class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of base classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived Class")
    def printStr(self):
        print("Countries:", self.str1, "", self.str2)
obj = Derived()
obj.printStr()

"""
Output:
Base1 Class
Base2 Class
Derived Class
Countries: USA  Germany
"""