# coding=utf-8
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格


# 递归
def trim(s: str) -> str:
    if len(s) == 0:
        return s

    if s[0] == ' ':
        return trim(s[1:])

    if s[-1] == ' ':
        return trim(s[:-1])

    return s


# 非递归
def trim_normal(s: str) -> str:
    while (len(s) > 0 and s[0] == ' '):
        s = s[1:]

    while (len(s) > 0 and s[-1] == ' '):
        s = s[:-1]

    return s
