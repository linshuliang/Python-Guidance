# coding=utf-8


def convert2int(var) -> int:
    try:
        return int(var)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    convert2int("xyz")
