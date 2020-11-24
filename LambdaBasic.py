def my_lambda():
    return lambda a: a + 10


def my_lambda_with_multi():
    return lambda a, b: a * b


def my_func(n):
    return lambda a: a * n


if __name__ == "__main__":
    x = my_lambda()
    print(x(5))
    x = my_lambda_with_multi()
    print(x(5, 6))
    x = my_func(2)
    print(x(5))


