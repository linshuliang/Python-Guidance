# git 删除本地和远程分支

## Step 1: 切换到要操作的项目文件夹

```
cd ProjectPath
```

## Ste 2: 查看项目的分支们(包括本地和远程)

```
git branch -a
```

## Step 3: 删除本地分支

```
git branch -d BranchName
```

## Step 4: 删除远程分支

```
git push origin --delete BranchName
```

## Step 5: 查看删除后分支们

```
git branch -a
```
