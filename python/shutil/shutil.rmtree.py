# coding=utf-8
import os
import shutil

# 递归地创建目录
dir_path = 'a/b/c/d'
os.makedirs(dir_path)

# 递归地删除目录
shutil.rmtree('a')
