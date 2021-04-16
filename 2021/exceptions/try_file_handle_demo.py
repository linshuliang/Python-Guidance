# coding=utf-8
import os

try:
    file_name = "test_open.txt"
    fh = open(file_name, "w")
    fh.write("Test : try-except-else \n")
except IOError as e:
    print(e)
else:
    print("Success : Open File %s" % file_name)
    fh.close()
    os.system("cat %s" % file_name)
    os.remove(file_name)
