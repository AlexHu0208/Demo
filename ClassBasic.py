class MyClass:
    x = 5


class MyPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print("Hello, my name is {}".format(self.name))


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome {} {} to the class of {}".format(self.fname, self.lname, self.graduation_year))


if __name__ == "__main__":
    myClass = MyClass()
    print(myClass.x)
    myPerson = MyPerson("ABC", 20)
    print(myPerson.name, myPerson.age)
    myPerson.my_func()
    x = Person("Alex", "Hu")
    x.print_name()
    x = Student("ABC", "DEF", 2020)
    x.print_name()
    x.welcome()
