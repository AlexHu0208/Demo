def tuple_basic():
    my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    print(my_tuple)
    print(len(my_tuple))
    print(type(("apple",)))
    print(type(("apple")))
    print(my_tuple[1])
    print(my_tuple[-1])
    print(my_tuple[2:5])
    print(my_tuple[::2])
    print(my_tuple[:4])
    print(my_tuple[2:])
    print(my_tuple[-4:-1])
    print("apple" in my_tuple)


def tuple_unpack_basic():
    fruits = ("apple", "banana", "cherry")
    (green, yellow, red) = fruits
    print(green)
    print(yellow)
    print(red)
    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
    (green, yellow, *red) = fruits
    print(green)
    print(yellow)
    print(red)
    (green, *tropic, red) = fruits
    print(green)
    print(tropic)
    print(red)


def tuple_join_basic():
    tuple1 = ("a", "b", "c")
    tuple2 = (1, 2, 3)
    tuple3 = tuple1 + tuple2
    print(tuple3)
    fruits = ("apple", "banana", "cherry")
    my_tuple = fruits * 2
    print(my_tuple)


if __name__ == "__main__":
    # tuple_basic()
    # tuple_unpack_basic()
    tuple_join_basic()