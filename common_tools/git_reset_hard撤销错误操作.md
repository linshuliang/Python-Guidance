# git pull 撤销错误操作

## Step 1. git reflog 命令查看历史变更记录：

```
[lsl@:Python-Guidance]git reflog

fdb70fe HEAD@{0}: pull origin newpbft: Fast-forward
40a9a83 HEAD@{1}: checkout: moving from guan to master
b3fa4c3 HEAD@{2}: commit: copy from newpbft, first init
```

## Step 2. git reset --hard 回退

```
git reset --hard 40a9a83
```
