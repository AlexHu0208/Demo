import re


def regex_basic():
    txt = "The rain in Spain"
    x = re.findall("ai", txt)
    print(x)
    x = re.findall("Portugal", txt)
    print(x)
    x = re.search("\s", txt)
    print(x)
    x = re.search("Portugal", txt)
    print(x)
    x = re.split("\s", txt)
    print(x)
    x = re.split("\s", txt, 1)
    print(x)
    x = re.sub("\s", "9", txt)
    print(x)
    x = re.sub("\s", "9", txt, 2)
    print(x)
    x = re.search(r"\bS\w+", txt)
    print(x.span())
    print(x.string)
    print(x.group())


if __name__ == "__main__":
    regex_basic()
