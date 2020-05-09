# queue 模块

在 FIFO 数据结构中，将首先处理添加到队列中的第一个元素。

队列是典型的 FIFO 数据结构。插入操作也称作入队，新元素始终被添加在队列的末尾。
删除操作也被称为出队。 你只能移除第一个元素。

## 队列分类

| 队列方式            | 特点         |
| :-----------        | :----------- |
| queue.Queue	      | 先进先出队列 |
| queue.LifoQueue     |	后进先出队列 |
| queue.PriorityQueue |	优先级队列   |
| queue.deque	      | 双线队列     |

## 队列的方法

| 方法                | 用法说明         |
| :-----------        | :-----------     |
| put	              | 放数据，Queue.put( )默认有block=True和timeout两个参数。当block=True时，写入是阻塞式的，阻塞时间由timeout确定。当队列q被（其他线程）写满后，这段代码就会阻塞，直至其他线程取走数据。Queue.put（）方法加上 block=False 的参数，即可解决这个隐蔽的问题。但要注意，非阻塞方式写队列，当队列满时会抛出 exception Queue.Full 的异常 |
| get	              | 取数据(默认阻塞),Queue.get([block[, timeout]])获取队列，timeout等待时间 |
| empty	              | 如果队列为空，返回True，反之False |
| qsize	              | 显示队列中真实存在的元素长度 |
| maxsize	          | 最大支持的队列长度,使用时无括号 |
| join	              | 实际上意味着等到队列为空，再执行别的操作 |
| task\_done	      | 在完成一项工作之后，Queue.task\_done()函数向任务已经完成的队列发送一个信号 |
| full	              | 如果队列满了，返回True，反之False |
