# 列表中找最大最小值


def findMinAndMax(L: list) -> tuple:
    if L == []:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if i < min:
                min = i
            elif i > max:
                max = i

    return (min, max)


def BuildInFindMinAndMax(L: list) -> tuple:
    if L == []:
        return (None, None)
    else:
        minElement = min(L)
        maxElement = max(L)
        return (minElement, maxElement)


if __name__ == "__main__":
    if BuildInFindMinAndMax([]) != (None, None):
        print('测试失败!')
    elif BuildInFindMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif BuildInFindMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif BuildInFindMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')
