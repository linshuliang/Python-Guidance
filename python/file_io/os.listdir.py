# coding=utf-8
import os

cwd = os.getcwd()
dir_files = os.listdir(cwd)

for file_name in dir_files:
    print(file_name)
