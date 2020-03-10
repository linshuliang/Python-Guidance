# coding=utf-8
# os.makedirs() 方法用于递归创建目录，
# 但创建的所有 intermediate-level 文件夹需要包含子目录。
# 语法：os.makedirs(path, mode=0777)
import os

cwd = os.getcwd()
new_dir = os.path.join(cwd, 'new/dir/1/')

os.makedirs(new_dir, 0o721)
