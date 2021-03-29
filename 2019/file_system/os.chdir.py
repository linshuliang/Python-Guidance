# coding=utf-8
import os

cwd = os.getcwd()
print('Current Working Directory is: {}'.format(cwd))

# 切换工作目录
previous_working_directory = '..'
os.chdir(previous_working_directory)

cwd = os.getcwd()
print('Now Current Working Directory is: {}'.format(cwd))
