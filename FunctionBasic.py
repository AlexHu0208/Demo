def my_function():
    print("Hello from a function")


def my_function_with_params(fname):
    print("{} Refsnes".format(fname))


def my_function_with_multi(*kids):
    print("The youngest child is {}".format(kids[2]))


def my_function_with_key(a3, a2, a1):
    print("The youngest child is {}".format(a3))


def my_function_with_arbitrary(**kid):
    print("His last name is {}".format(kid["lname"]))


def my_function_with_default(country="Canada"):
    print("I am from {}".format(country))


def my_function_with_list(food):
    [print(x) for x in food]


def my_function_with_return(x):
    return 5 * x


def my_function_with_pass():
    pass


def my_function_recursion(x):
    def recursion(k):
        if k > 0:
            result = k + recursion(k - 1)
            print(result)
        else:
            result = 0
        return result
    return recursion(x)


if __name__ == "__main__":
    my_function()
    my_function_with_params("Email")
    my_function_with_multi("A", "B", "C")
    my_function_with_key(a1="A", a2="B", a3="C")
    my_function_with_arbitrary(lname="C", fname="B")
    my_function_with_default("China")
    my_function_with_default()
    my_function_with_list(["A", "B", "C"])
    print(my_function_with_return(12))
    my_function_recursion(5)



