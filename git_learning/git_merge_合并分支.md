# git 合并分支

## 查看所有分支 git branch -a

```
git branch -a
```

显示：

```
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/v1.2
  remotes/origin/master
  remotes/origin/v1.1
  remotes/origin/v1.0
```

## 切换分支

比如想将 v1.1 合并到 v1.2 中，则先切换分支:

```
git checkout v1.1
git checkout v1.2
```

## 在分支上执行 git merge

在分支 v1.2 中执行 git merge

```
git merge v1.1
```

## 提交代码

如果没有报错，则 git commit v1.2

```
git commit origin v1.2
```

如果报 conflict 了，则解决冲突后再 commit.
