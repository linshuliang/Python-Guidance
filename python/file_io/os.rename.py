# coding=utf-8
import os

cwd = os.getcwd()

new_dir = 'new_dir'
os.makedirs(new_dir)

print('Files list in current working directory.')
print(os.listdir(cwd))

os.rename(new_dir, 'rename')

print('Files list in current working directory.')
print(os.listdir(cwd))

os.removedirs('rename')
