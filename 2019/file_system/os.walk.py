# coding=utf-8
"""
def walk(top, topdown=True, onerror=None, followlinks=False)
    Args:
	    top (str): 遍历目录的路径
	    topdown (bool): 当为 True, 由上至下遍历目录；当为 False, 由下至上遍历目录

	:Returns: 返回一个生成器，可用 for 语句循环。每次 yield 一个 3-元组: (dirpath, dirnames, filenames):
		dirpath:   为当前目录的路径；
		dirnames:  当前目录中的子目录的名称；
		filenames: 当前目录中的文件的名称
"""
import os

path = '..'
path = os.path.abspath(path)

for dir_path, subdirs_name, files_name in os.walk(path):
    print('Current directory: {}'.format(dir_path))
    print('Names of sub directory in cwd: {}'.format(subdirs_name))
    print('Name of sub file in cwd: {}'.format(files_name))
    print('#' * 100)

# 收集所有文件的路径
file_path_list = list()
for dir_path, subdirs_name, files_name in os.walk(path):
    for file_name in files_name:
        file_path_list.append(os.path.join(dir_path, file_name))

print(file_path_list)
