# coding=utf-8
# 语法：os.remove(path)
#       path：要移除的文件路径
# 注：只能删文件，不能删目录
import os

# create a file
cwd = os.getcwd()
new_file_name = os.path.join(cwd, 'os.remove_file.txt')
new_file = open(new_file_name, 'a')
new_file.close()
print('Creating new file: {}'.format(new_file_name))

# delete a file
os.remove(new_file_name)
print('The file {} is deleted'.format(new_file_name))
