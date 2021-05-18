import urllib.request

myURL = urllib.request.urlopen("https://www.runoob.com/")

# readline() ：读取文件的一行
print(myURL.readline())
