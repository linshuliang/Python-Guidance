# coding=utf-8
import os

cwd = os.getcwd()
file_name = os.listdir(cwd)[0]
file_name = os.path.join(cwd, file_name)

if os.path.exists(file_name):
    # 如果文件存在，执行 if 后面的语句
    if os.path.isfile(file_name):
        print('{} is a file.'.format(file_name))
    elif os.path.isdir(file_name):
        print('{} is a directory.'.format(file_name))

    # base name
    file_basename = os.path.basename(file_name)
    print('basename of {} is {}'.format(file_name, file_basename))

    # directory name
    file_dirname = os.path.dirname(file_name)
    print('dirname of {} is {}'.format(file_name, file_dirname))

    # os.path.name
    if os.path.join(file_dirname, file_basename) == file_name:
        print("{} is equal os.path.join({}, {})".format(file_name, file_dirname,
                                                        file_basename))

    # os.path.split
    split_tuple = os.path.split(file_name)
    print(split_tuple)

    # os.path.splitext
    file_path, file_ext = os.path.splitext(file_name)
    print(file_path, file_ext)
