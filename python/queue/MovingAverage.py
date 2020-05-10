# coding=utf-8


class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.queue = list()

    def next(self, val):
        self.queue.append(val)
        # calculate the sum of moving average
        window_sum = sum(self.queue[-self.size:])
        return window_sum / min(len(self.queue), self.size)


if __name__ == '__main__':
    ma = MovingAverage(3)
    for i in range(10):
        print(ma.next(i))
