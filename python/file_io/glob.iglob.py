# coding=utf-8
import os
import glob

cwd = os.getcwd()
path = os.path.abspath(cwd)

for dir_name, subdirs_name, files_name in os.walk(path):
    # `*` 号匹配0个或多个字符
    # 找出所有以 .py 结尾的文件
    find_pathname = os.path.join(dir_name, '*.py')
    print(find_pathname)
    py_path_generator = glob.glob(find_pathname)
    print('*' * 100)
    for py_path in py_path_generator:
        print(py_path)

    # `?` 匹配单个字符
    find_pathname = os.path.join(dir_name, 'os.listd?r.py')
    special_path_generator = glob.iglob(find_pathname)
    print('?' * 100)
    for special_path in special_path_generator:
        print(special_path)

    # `[]` 匹配指定范围中的字符
    find_pathname = os.path.join(dir_name, '[g-o]*')
    range_generator = glob.iglob(find_pathname)
    print('[]' * 100)
    for range_path in range_generator:
        print(range_path)
