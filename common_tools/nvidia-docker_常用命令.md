# nvidia-docker 常用命令

* 容器：container
* 镜像：image

## 1 查看当前正在运行的容器

```
nvidia-docker ps
```

## 2 对于已退出的容器，可以使用如下命令进行查看

```
nvidia-docker ps -a
```

## 3 删除容器

```
nvidia-docker rm container_id
```

## 4 删除镜像

```
nvidia-docker rm image_id
```

## 5 创建新的容器

```
sudo nvidia-docker run --name container_name -v /PATH/TO/DIR/:/server_share --network=host -it image_id /bin/bash
```

## 6 列出所有镜像

```
nvidia-docker images
```

## 7 将容器打包成镜像

```
nvidia-docker commit 容器_id 镜像_name
```

## 8 Docker 退出容器但不关闭当前容器

方法一：如果要正常退出不关闭容器，请按 Ctrl+P+Q 进行退出容器。

方法二：如果使用 exit 退出，那么在退出之后会关闭容器，可以使用下面的流程进行恢复:

```
nvidia-docker restart container_name
nvidia-docker attach container_name
```
