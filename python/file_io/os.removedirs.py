# coding=utf-8
# os.makedirs() 方法用于递归创建目录，
# 但创建的所有 intermediate-level 文件夹需要包含子目录。
# 语法：os.makedirs(path, mode=0o777)
import os

cwd = os.getcwd()
new_dir = os.path.join(cwd, 'new/dir/1/')

# 创建目录
os.makedirs(new_dir, 0o721)

# os.walk
for dir_path, subdirs_name, files_name in os.walk(cwd):
    print('Current directory: {}'.format(dir_path))
    print('Names of sub directory in cwd: {}'.format(subdirs_name))
    print('Name of sub file in cwd: {}'.format(files_name))
    print('#' * 100)
    print('\n')

# 递归地删除目录
os.removedirs(new_dir)

# os.walk
for dir_path, subdirs_name, files_name in os.walk(cwd):
    print('Current directory: {}'.format(dir_path))
    print('Names of sub directory in cwd: {}'.format(subdirs_name))
    print('Name of sub file in cwd: {}'.format(files_name))
    print('#' * 100)
    print('\n')
