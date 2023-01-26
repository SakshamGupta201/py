class MyClass:
    def __init__(self, value) -> None:
        self._value = value

    def show(self):
        print(self._value)
    
    @property
    def ten_value(self):
        return 10 * self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10


a = MyClass(34)
a._value = 67
a.show()
