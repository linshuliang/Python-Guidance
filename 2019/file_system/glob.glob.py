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
    py_path_list = glob.glob(find_pathname)
    print('*' * 100)
    print(py_path_list)

    # `?` 匹配单个字符
    find_pathname = os.path.join(dir_name, 'os.listd?r.py')
    special_path_list = glob.glob(find_pathname)
    print('?' * 100)
    print(special_path_list)

    # `[]` 匹配指定范围中的字符
    find_pathname = os.path.join(dir_name, '[g-o]*')
    special_range_list = glob.glob(find_pathname)
    print('[]' * 100)
    print(special_range_list)
