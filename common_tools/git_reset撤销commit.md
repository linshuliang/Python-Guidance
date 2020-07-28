# git reset

## git commit 后撤销

```shell
git reset --选项 [历史记录]
```



**例如**

撤回一次 commit

```shell
git reset --soft HEAD~1
```



撤回两次 commit

```shell
git reset --soft HEAD~2
```



**选项说明**

* `--mixed`: 不删除工作空间改动代码，撤销 commit，并撤销 git ad 操作；

* `--soft` : 不删除工作空间改动代码，撤销 commit，不撤销 git add；
* `--hard`: 删除工作空间改动代码，撤销 commit，撤销 git add，`git reset --hard`后就恢复到上一次commit状态了；



## git pull 撤销错误操作

**Step 1** git reflog 命令查看历史变更记录：

```shell
[lsl@:Python-Guidance]git reflog

fdb70fe HEAD@{0}: pull origin newpbft: Fast-forward
40a9a83 HEAD@{1}: checkout: moving from guan to master
b3fa4c3 HEAD@{2}: commit: copy from newpbft, first init
```



**Step 2** git reset --hard 回退

```shell
git reset --hard 40a9a83
```
