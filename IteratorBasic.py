def iter_basic():
    my_tuple = ("apple", "banana", "cherry")
    my_it = iter(my_tuple)
    print(next(my_it))
    print(next(my_it))
    print(next(my_it))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


def iter_create_basic():
    myNumbers = MyNumbers()
    myIter = iter(myNumbers)
    for x in myIter:
        print(x)


if __name__ == "__main__":
    iter_basic()
    iter_create_basic()
