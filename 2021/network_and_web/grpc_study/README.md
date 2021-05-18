# gRPC

`gRPC` (Google RPC) 是 Google 发起的一个开源`RPC`系统。
该系统基于`HTTP`协议传输，使用`Protocol Buffers`作为接口描述语言。

`gRPC`最常见的应用场景：

* 微服务框架下，多种语言服务之间的高效交互；
* 将手机服务、浏览器连接至后台；
* 产生高效的客户端库；

## 1 远程过程调用 - RPC

远程过程调用 (`Remote Procedure Call`，缩写为 `RPC`) 是一个计算机通信协议。
该协议允许运行于一台计算机的程序调用另一个地址空间的子程序，
而程序员就像调用本地程序一样，无需额外地为这个交互作用编程。

`RPC`是一种客户端-服务器(`Client/Server`)模式，
经典实现是一个通过`发送请求 - 接受回应`进行信息交互的系统。

`RPC` 是一种进程间通信的模式，程序分布在不同的地址空间中：

* 在同一主机里，`RPC`可通过不同的**虚拟地址空间**进行通讯；
* 在不同主机里，`RPC`可通过不同的**物理地址**进行通讯；

### 1.1 RPC 中的信息传递

远程过程调用(`RPC`)是一个**分布式计算**的`客户端-服务器(Client-Server)`的例子。
远程过程调用总是**由客户端对服务器发出一个执行若干过程的请求**，并用客户端提供的参数，
执行结果将返回给客户端。

`RPC` 流程：

* 客户端调用，这个调用是在本地，并将客户端提供的调用参数`push`到栈(`stack`)中；
* 客户端包装这些参数，打包的过程称为 `marshalling`，常见方式：`XML`、`JSON`、`二进制编码`；
* 客户端本地操作系统发送信息到服务器（可通过自定义`TCP协议`或`HTTP`传输）；
* 服务器系统将信息传送到服务端 stub；
* 服务端 stub 解析信息，解析的过程称为`unmarshalling`；
* 服务端 stub 调用程序，并将结果传送到服务器系统，然后再传送到客户端。

## 2 gRPC - Python Demo

### 2.1 protobuf 安装

到[protobuf Release](https://github.com/protocolbuffers/protobuf/releases)中
下载最新的`protoc-*-osx-x86_x64.zip` ：

```shell
wget https://github.com/protocolbuffers/protobuf/releases/download/v3.17.0/protoc-3.17.0-osx-x86_64.zip
```

解压，拷贝到`$PATH`下：

```shell
unzip protoc-3.17.0-osx-x86_64.zip -d protoc-3.17.0
cd protoc-3.17.0
sudo cp -r include/ /usr/local/include/
sudo cp -r bin/ /usr/local/bin/
```

测试：

```shell
protoc
```

### 2.2 定义 `.proto` 文件

```proto
// helloworld.proto
syntax = "proto3";

package helloworld;

// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}
```

然后调用`protoc`命令编译生成：

```shell
protoc -I=. --python_out=. ./helloworld.proto
```

`protoc`编译命令解析：

* `-I` ：指定编译源文件所在的目录；
* `--python_out` ：指定生成 `*_pb2.py` 文件的路径；

上述生成的`helloworld_pb2.py`中包含了类`Request`和类`Reply`的定义。
如果要生成`grpc`的客户端`client`类和服务端`server`类的代码，需执行：

```shell
python -m grpc_tools.protoc -I=. --grpc_python_out=. ./helloworld.proto
```

* 执行此命令，需先`pip`安装`grpcio`和`grpcio-tools`。
* 执行命令`python -m grpc_tools.protoc`将生成`*_pb2_grpc.py`文件，此文件中包含了客户端(`client`)类和服务端(`server`)类的定义。

## 参考

* [维基百科 - RPC](https://zh.wikipedia.org/wiki/%E9%81%A0%E7%A8%8B%E9%81%8E%E7%A8%8B%E8%AA%BF%E7%94%A8)
* [维基百科 - 分布式计算](https://zh.wikipedia.org/wiki/%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97)
* [维基百科 - 客户端-服务器](https://zh.wikipedia.org/wiki/%E4%B8%BB%E5%BE%9E%E5%BC%8F%E6%9E%B6%E6%A7%8B)
