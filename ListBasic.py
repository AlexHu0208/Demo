def list_basic():
    my_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(my_list)
    print(len(my_list))
    print(type(my_list))
    print(my_list[1])
    print(my_list[-1])
    print(my_list[2:5])
    print(my_list[:4])
    print(my_list[2:])
    print(my_list[-4:-1])
    print(my_list[::2])
    print("apple" in my_list)


def list_change_basic():
    my_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    my_list[1] = "blackcurrant"
    print(my_list)
    my_list[1] = ["blackcurrant", "watermelon"]
    print(my_list)
    my_list[1:3] = ["blackcurrant", "watermelon"]
    print(my_list)
    my_list.insert(2, "blueberry")
    print(my_list)


def list_add_basic():
    my_list = ["apple", "banana", "cherry"]
    my_list.append("orange")
    print(my_list)
    tropical = ["mongo", "pineapple", "papaya"]
    my_list.extend(tropical)
    print(my_list)
    my_tuple = ["kiwi", "blueberry"]
    my_list.extend(my_tuple)
    print(my_list)


def list_remove_basic():
    my_list = ["apple", "banana", "cherry"]
    my_list.remove("banana")
    print(my_list)
    del my_list[0]
    print(my_list)
    my_list.clear()
    print(my_list)


def list_pop_basic():
    my_list = ["apple", "banana", "cherry"]
    my_list.pop(1)
    print(my_list)
    my_list.pop()
    print(my_list)


def list_loop_basic():
    my_list = ["apple", "banana", "cherry"]
    for x in my_list:
        print(x)
    for i in range(len(my_list)):
        print(my_list[i])
    [print(x) for x in my_list]


def list_comprehension_basic():
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    my_list = [x for x in fruits if "a" in x]
    print(my_list)
    my_list = [x if x != "banana" else "orange" for x in fruits]
    print(my_list)


def list_sort_basic():
    my_list = [100, 50, 65, 82, 23]
    my_list.sort()
    print(my_list)
    my_list.sort(reverse=True)
    print(my_list)
    my_list.sort(key=lambda x: abs(x - 50))
    print(my_list)
    my_list.reverse()
    print(my_list)


def list_copy_basic():
    my_list = ["apple", "banana", "cherry"]
    new_list = my_list.copy()
    print(new_list)


def list_join_basic():
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    list3 = list1 + list2
    print(list3)
    list1.extend(list2)
    print(list1)


if __name__ == "__main__":
    # list_basic()
    # list_change_basic()
    # list_add_basic()
    # list_remove_basic()
    # list_pop_basic()
    # list_loop_basic()
    # list_comprehension_basic()
    # list_sort_basic()
    # list_copy_basic()
    list_join_basic()
