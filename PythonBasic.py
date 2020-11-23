import random


# Python basic
def variable_basic():
    x = 5
    y = "John"
    print(x)
    print(y)


def type_basic():
    x = 5
    print(type(x))
    y = dict(name="John", age=36)
    print(y)


def number_basic():
    x, y, z = 5, 1.0, 1 + 2j
    print(x)
    print(y)
    print(z)
    print(type(x))
    print(type(y))
    print(type(z))


def random_basic():
    print(random.randrange(1, 10))


def cast_basic():
    x = int(1)
    y = float("1")
    z = str(1)
    print(x)
    print(y)
    print(z)


def string_basic():
    b = "Hello world!"
    print(b[1])
    print(b[2:5])
    print(b[-5:-2])
    print(len(b))
    print(b.lower())
    print(b.upper())
    print(b.split(" "))
    print("Hello" in b)
    print(b.replace("o", "q"))
    quantity = 3
    item = 567
    price = 49.95
    order = "I want to pay {2} dollars for {0} pieces of item {1}."
    print(order.format(quantity, item, price))


def string_function_basic():
    a = "Hello world!"
    print(a.capitalize())
    print(a.casefold())
    print(a.count("o"))
    print(a.encode())
    print(a.endswith("world!"))
    print(a.expandtabs(4))
    print(a.index("e"))
    print(a.swapcase())
    print(a.title())


if __name__ == "__main__":
    # variable_basic()
    # type_basic()
    # number_basic()
    # random_basic()
    # cast_basic()
    string_basic()
    string_function_basic()
