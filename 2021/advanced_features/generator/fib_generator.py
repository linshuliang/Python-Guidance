def fib(maxLimit=100):
    a, b = 0, 1
    while (a < maxLimit):
        a, b = b, a + b
        yield a


if __name__ == "__main__":
    f_gen = fib(200)
    for item in f_gen:
        print(item)
