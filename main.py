class Employee:
    no_of_leaves = 8

    def __init__(self) -> None:
        pass

    @classmethod
    def changeLeaves(cls, leaves):
        cls.no_of_leaves = leaves

    def printLeaves(self):
        print(self.no_of_leaves)


emp = Employee()
emp.printLeaves()
emp.changeLeaves(23)
emp.printLeaves()


