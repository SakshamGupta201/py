class Person:
    def __init__(self, name) -> None:
        self.name = name

    def info(self):
        print(f"My name is {self.name}")

a = Person("Saksham")
a.info()
