x: int = 10
def func():
    global x
    x = 12.0
func()
print(type(x))