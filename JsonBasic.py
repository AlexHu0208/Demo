import json
from MyModule import person

x = '{ "name":"John", "age":30, "city":"New York"}'


def json_basic():
    print(json.dumps({"name": "John", "age": 30}))
    print(json.dumps(["apple", "bananas"]))
    print(json.dumps(("apple", "bananas")))
    print(json.dumps("hello"))
    print(json.dumps(42))
    print(json.dumps(31.76))
    print(json.dumps(True))
    print(json.dumps(False))
    print(json.dumps(None))


if __name__ == "__main__":
    y = json.loads(x)
    print(y["age"])
    y = json.dumps(person)
    print(y)
    json_basic()
    y = json.dumps(person, indent=4)
    print(y)
    y = json.dumps(person, indent=4, separators=(". ", " = "))
    print(y)
    y = json.dumps(person, indent=4, sort_keys=True)
    print(y)



