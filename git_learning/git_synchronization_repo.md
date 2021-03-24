# 更新 GitHub 中fork 出來的repository

从GitHub 上面fork 出来的repository，整个状态会停留在当初fork 的时候，后面的同步要靠自己动手，
当然你也可以把fork出来的repository 整个砍掉重新fork，这边要讲的是手动同步、而不用砍掉重练的方法。
有两个不同的git server要做同步的动作也是这样做。

操作环境: 已经把你fork出来的repository给clone到自己的电脑上了，
clone 好之后请切换到对应的资料夹底下，然后就可以开始使用 git 做操作了。


## Step 1: 添加 upstream

第一次操作时我们要加入一个远端的 remote 当作更新来源，如果要比较是否有加入成功的话可以在操作前后先看状态：

```
git remote -v
```

预设只有 origin 这个 remote:

```
origin https://github.com/user/repo.git (fetch)
origin https://github.com/user/repo.git (push)
```

加入远端的repository，在这边的情境也就是比较新的、上游的repository upstream，后面那串网址是repository 位置：

```
$ git remote add upstream https://github.com/otheruser/repo.git
```

这时，现有的remote端多了两组 upstream（fetch 和 push)

```
$ git remote -v
origin https://github.com/user/repo.git (fetch)
origin https://github.com/user/repo.git (push)
upstream https://github.com/otheruser/repo.git (fetch)
upstream https://github.com/otheruser/repo.git (push)
```

## Step 2: 切分支，并将 upstream 的分支拉进来

假如我要做更新的的 branch 是 master 的话就先切到 master branch：

```
git checkout master
```

接着把 upstream 的 master branch 拉进来：

```
git pull upstream master
```

如果你的 master branch 有自己的 commit, 也可以用 rebase 來避免不必要的 merge 操作：

```
git pull --rebase upstream master
```

## Step 3: push 更新

如果没有发生冲突的话这样应该就完成了本地的更新，再把更新后的 branch push 出去就行了：

```
git push origin master
```
