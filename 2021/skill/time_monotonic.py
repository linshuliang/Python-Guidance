import time

for i in range(10):
    start = time.monotonic()
    time.sleep(i)
    end = time.monotonic()
    print("current time: %s" % end)
    print("time flies %s s: " % (end - start))

#  time.monotonic() 它总是回传前进的值，可理解成开机时间到现在的时间。
# https://shengyu7697.github.io/python-use-time-monotonic/
