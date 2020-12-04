class Class1(object):
    x = 10
    y = 20
    z = None

    def sum(self):
        x = 300
        y = 200
        print(f"{x} {y}")
        print(f"{self.x} {self.y}")
        self.z = "Arif"
        print(self.z)


class Class2:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __del__(self):
        print("object delete is called and this object is deleted")

    def sum(self):
        ans = self.y + self.z
        print(f"{self.x} {ans}")


# creat object of class1
obj = Class1()
obj.sum()
obj.x = 30
obj.y = 40
obj.sum()

# create object of class2
obj2 = Class2("Arif", 13, 14)
obj2.sum()

del obj2



