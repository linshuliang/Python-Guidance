# coding=utf-8
b = 5


def test_2():
    global b
    b = 1
    print('In func test_2: b = %d' % b)


test_2()
print('global b = %d' % b)
