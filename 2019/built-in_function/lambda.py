# coding=utf-8
# lambda 是为了减少单行函数的定义而存在的。
# lambda 并不会带来程序运行效率的提高，只会使代码更简洁。

# Syntax
#   lambda arguments : expression

add_fn = lambda a: a + 10

number = float(input('Please input a number:'))
print(add_fn(number))

# lambda expression can take any number of arguments
add_func = lambda a, b: a + b
print(add_func(3, 5))
