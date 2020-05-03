# macbook 科学上网

## 安装 Homebrew

* Step1: 打开网络偏好设置 --> 高级 --> 代理 --> SOCKS 代理--> 查看 SOCKS 代理服务器的地址，例如127.0.0.0.1:1080
* Step2: 配置 ~/.gitconfig

```shell
git config --global http.https://github.com.proxy socks5://127.0.0.1:1080
git config --global https.https://github.com.proxy socks5://127.0.0.1:1080
```

* Step3: 安装 Homebrew

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
