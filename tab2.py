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


obj = Class1()
obj.sum()
obj.x = 30
obj.y = 40
obj.sum()
