# coding=utf-8
import sys
import traceback

try:
    raise ValueError("ValueError: raise")
except ValueError as e:
    print(e)
    print("=" * 20)

    ex_type, ex_val, ex_traceback = sys.exc_info()
    print(ex_type)  # 异常类型
    print(ex_val)  # 异常值
    for s in traceback.extract_tb(ex_traceback):
        print(s)  # 异常的堆栈信息
