# ps 进程查看器

Linux中的ps命令是Process Status的缩写。
ps命令用来列出系统中当前运行的进程。

如果想要动态的显示进程信息，就可以使用 top 命令。

## 输出列的含义

* USER : 用户名  
* UID : 进程被该 UID 所拥有
* PID : 进程的ID
* %CPU : CPU 使用的资源百分比
* %MEM : 占用的记忆体使用率
* VSZ ：占用的虚拟记忆体大小
* RSS : 占用的记忆体大小
* TTY : 终端的次要装置号码 (minor device number of tty)
* STAT : 该行程的状态
* START : 进程的开始时间
* TIME : 执行的时间
* COMMAND : 进程对应的执行指令

## 常用命令


*(1) 列出目前内存中所有正在运行的程序*

```
[root@localhost test6]# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0  10368   676 ?        Ss   Nov02   0:00 init [3]
root         2  0.0  0.0      0     0 ?        S<   Nov02   0:01 [migration/0]
root         3  0.0  0.0      0     0 ?        SN   Nov02   0:00 [ksoftirqd/0]
root         4  0.0  0.0      0     0 ?        S<   Nov02   0:01 [migration/1]
root         5  0.0  0.0      0     0 ?        SN   Nov02   0:00 [ksoftirqd/1]
root         6  0.0  0.0      0     0 ?        S<   Nov02  29:57 [events/0]
root         7  0.0  0.0      0     0 ?        S<   Nov02   0:00 [events/1]
root         8  0.0  0.0      0     0 ?        S<   Nov02   0:00 [khelper]
root        49  0.0  0.0      0     0 ?        S<   Nov02   0:00 [kthread]
root        54  0.0  0.0      0     0 ?        S<   Nov02   0:00 [kblockd/0]
root        55  0.0  0.0      0     0 ?        S<   Nov02   0:00 [kblockd/1]
root        56  0.0  0.0      0     0 ?        S<   Nov02   0:00 [kacpid]
```

*(2) 显示所有进程信息，连同命令行*

```
[root@localhost test6]# ps -ef
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 Nov02 ?        00:00:00 init [3]
root         2     1  0 Nov02 ?        00:00:01 [migration/0]
root         3     1  0 Nov02 ?        00:00:00 [ksoftirqd/0]
root         4     1  0 Nov02 ?        00:00:01 [migration/1]
root         5     1  0 Nov02 ?        00:00:00 [ksoftirqd/1]
root         6     1  0 Nov02 ?        00:29:57 [events/0]
root         7     1  0 Nov02 ?        00:00:00 [events/1]
root         8     1  0 Nov02 ?        00:00:00 [khelper]
root        49     1  0 Nov02 ?        00:00:00 [kthread]
root        54    49  0 Nov02 ?        00:00:00 [kblockd/0]
root        55    49  0 Nov02 ?        00:00:00 [kblockd/1]
root        56    49  0 Nov02 ?        00:00:00 [kacpid]
```

*(3) 显示指定用户信息*

```
[root@localhost test6]# ps -u root
PID TTY          TIME CMD
1 ?        00:00:00 init
2 ?        00:00:01 migration/0
3 ?        00:00:00 ksoftirqd/0
4 ?        00:00:01 migration/1
5 ?        00:00:00 ksoftirqd/1
6 ?        00:29:57 events/0
7 ?        00:00:00 events/1
8 ?        00:00:00 khelper
49 ?        00:00:00 kthread
54 ?        00:00:00 kblockd/0
55 ?        00:00:00 kblockd/1
56 ?        00:00:00 kacpid
```

## 参考

[1] [Linux Tools Quick Tutorial](https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/ps.html)
