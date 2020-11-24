from MyModule import greeting, person
import platform

if __name__ == "__main__":
    greeting("Alex")
    print(person["age"])
    print(platform.system())
    print(dir(platform))
