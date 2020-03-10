# coding=utf-8
# 删除文件夹中名称不同，但内容相同的图片。
import os
from hashlib import md5

img_exts = ['jpg', 'jpeg', 'png', 'bmp', 'JPG', 'JPEG', 'PNG', 'BMP']


def main():
    images_dir = '/PATH/TO/Images_DIR'

    # list of images
    imgs_list = []
    for dirpath, subdirs_name, files_name in os.walk(images_dir):
        for file_name in files_name:
            file_path = os.path.join(dirpath, file_name)
            file_suffix = file_path.rsplit('.')[-1]
            if file_suffix in img_exts:
                imgs_list.append(file_path)

    # build the correspoding hash of images
    images_hash = []
    for img_path in imgs_list:
        hash = md5()
        img = open(img_path, 'rb')
        hash.update(img.read())
        img.close()
        images_hash.append((img_path, hash.hexdigest()))

    delete_num = 0
    # remove the duplicated images
    hash_num = len(images_hash)
    m = 0
    while m < hash_num:
        t = m + 1
        while t < hash_num:
            if images_hash[m][1] == images_hash[t][1]:
                print('Found Duplicated: {}'.format(images_hash[t][0]))
                os.remove(images_hash[t][0])
                del images_hash[t]
                hash_num -= 1
                delete_num += 1
            t += 1
        m += 1

    print('Number of delete images: {}.'.format(delete_num))


if __name__ == '__main__':
    main()
