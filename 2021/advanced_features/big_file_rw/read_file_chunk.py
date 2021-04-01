# 使用固定长度的缓冲区来不断读取文件内容


def read_file(fpath: str, block_size=1024):
    # 使用 with 语句 open 文件，结束/遇到异常 会自动 close 文件
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(block_size)
            if block:
                yield block
            else:
                return


if __name__ == "__main__":
    f_chunk = read_file("../README.md", 128)

    for chunk in f_chunk:
        print(chunk)
