def sandwich(func):
    def wrapper():

        print("Старт сендвича")
        func()
        print("конец")
    return wrapper

def meet(func):
    def wrapper():
        print("Mясо")
        func()
    return wrapper
@sandwich
@meet
def toppings():
    print("Some tomato")
    print("some banana")

send = toppings()

print(send)