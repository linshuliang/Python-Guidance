#!/bin/bash

set -v  # 打印出正在执行的命令，等价于 set -x
set -o nounset  # 如果遇到不存在的变量，则忽略它，等价于 set -u
set -o errexit  # 脚本只要发生错误，就终止执行，等价于 set -e
