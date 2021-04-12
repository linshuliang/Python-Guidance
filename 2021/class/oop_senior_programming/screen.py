# coding=utf-8


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise ValueError("width must be an integer")

        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise ValueError("width must be an integer")

        self._height = height

    @property
    def resolution(self):
        return self._width * self._height


if __name__ == "__main__":
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')
