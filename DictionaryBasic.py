def dictionary_basic():
    my_dict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(my_dict)
    print(my_dict["brand"])
    print(len(my_dict))
    print(type(my_dict))
    x = my_dict["model"]
    print(x)
    x = my_dict.get("model")
    print(x)
    x = my_dict.keys()
    print(x)
    my_dict["color"] = "white"
    print(x)
    x = my_dict.values()
    print(x)
    my_dict["year"] = 2000
    print(x)
    x = my_dict.items()
    print(x)
    my_dict.update({"year": 2005, "color": "red"})
    print(x)
    print("year" in my_dict)


def dictionary_remove_basic():
    my_dict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(my_dict)
    my_dict.pop("model")
    print(my_dict)
    my_dict.popitem()
    print(my_dict)
    del my_dict["brand"]
    print(my_dict)
    my_dict.clear()
    print(my_dict)


def dictionary_loop_basic():
    my_dict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    for x in my_dict:
        print(x, my_dict[x])
    for x in my_dict.keys():
        print(x)
    for x in my_dict.values():
        print(x)
    for x, y in my_dict.items():
        print(x, y)


if __name__ == "__main__":
    # dictionary_basic()
    # dictionary_remove_basic()
    dictionary_loop_basic()
