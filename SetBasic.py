def set_basic():
    my_set = {"apple", "banana", "cherry"}
    print(my_set)
    duplicate_set = my_set.copy()
    duplicate_set.add("cherry")
    print(duplicate_set)
    print(len(my_set))
    print(type(my_set))
    [print(x) for x in my_set]
    print("banana" in my_set)


def set_add_basic():
    my_set = {"apple", "banana", "cherry"}
    my_set.add("orange")
    print(my_set)
    tropical = {"pineapple", "mango", "papaya"}
    my_set.update(tropical)
    print(my_set)


def set_remove_basic():
    my_set = {"apple", "banana", "cherry"}
    my_set.remove("banana")  # will raise an error if "banana" doesn't exist
    print(my_set)
    my_set.add("banana")
    my_set.discard("banana")  # will NOT raise an error if "banana" doesn't exist
    print(my_set)
    x = my_set.pop()
    print(x)
    print(my_set)
    my_set.clear()
    print(my_set)


def set_join_basic():
    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}
    set3 = set1.union(set2)
    print(set3)
    set1.update(set2)
    print(set1)
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    z = x.intersection(y)
    print(z)
    z = x.symmetric_difference(y)
    print(z)
    z = x.difference(y)
    print(z)


if __name__ == "__main__":
    # set_basic()
    # set_add_basic()
    # set_remove_basic()
    set_join_basic()
