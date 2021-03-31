def f(x: int) -> int:
    return x * x


list_1 = [1, 2, 3]
r = map(f, list_1)

print(r)  # <map object>
print(list(r))  # [1, 4, 9]

cm = map(str, list_1)
print(list(cm))  # ['1', '2', '3']
