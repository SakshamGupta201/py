def greet(fx):
    def func(*args, **kwargs):
        print("Good morning")
        print(fx(*args, **kwargs))
        print("Thank you for using this fxn")
    return func

@greet
def add(a,b):
    return a+b

add(3,4) 