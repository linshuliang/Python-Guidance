# cuda 配置

## 查看 CUDA 和 cuDNN 版本

* 方法一： 使用 nvcc (NVIDIA (R) Cuda compiler driver) 来查看

```
nvcc --version
nvcc -V
```

* 方法二：查看文件

```
# 查找 cuda 安装路径
find / -name cuda
# 查看 cuda 版本
cat /usr/local/cuda/version.txt

# 查找 cudnn.h 的路径
find / -name cudnn.h
# 查看 cudnn 版本
 cat /usr/local/cuda-10.1/targets/x86_64-linux/include/cudnn.h | grep CUDNN_MAJOR -A 2
```

## 安装 nccl

[nccl 官网下载链接](https://developer.nvidia.com/nccl)

```
rpm -ivh nccl-repo-rhel7-2.5.6-ga-cuda10.1-1-1.x86_64.rpm

find / -name nccl.h
# nccl.h 路径: /usr/local/include/nccl.h

find / -name libnccl.so
# libnccl.so 路径: /usr/local/lib/libnccl.so

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib/
```
