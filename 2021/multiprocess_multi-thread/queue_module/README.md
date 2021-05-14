# queue

[queue](https://docs.python.org/zh-cn/3/library/queue.html) 模块实现了多生产者，多消费者队列。
这特别适用于多线程编程，保证消息安全地在多线程间交换。

## 1 队列分类

队列有很多种，但都依赖模块`queue`

| 队列方式               | 特点        |
| :-------------------- | :--------- |
| `queue.Queue`         | 先进先出队列 |
| `queue.LifoQueue`     | 后进先出队列 |
| `queue.PriorityQueue` | 优先级队列   |

```python
class queue.Queue(maxsize=0):
```

FIFO 队列，`maxsize`是个整数，用于设置可以放入队列中的项目数的上限。
当达到这个大小的时候，插入操作将阻塞，直到队列中的项目被消费掉。
如果`maxsize`小于等于零，队列尺寸为无限大。

```python
class queue.LifoQueue(maxsize=0):
```

LIFO 队列构造函数。

```python
class queue.PriorityQueue(maxsize=0):
```

优先级队列构造函数。最小值先被取出(最小值条目是由 `sorted(list(entries))[0]` 返回的条目)。

条目的典型模式是一个以下形式的元组：`(priority_number, data)`。

## 3 Queue 对象

队列对象 (Queue, LifoQueue, 或者 PriorityQueue) 提供下列描述的公共方法。

```python
qsize()
```

返回队列的大致大小。注意，qsize() > 0 不保证后续的 get() 不被阻塞，qsize() < maxsize 也不保证 put() 不被阻塞。

```python
empty()
```

如果队列为空，返回`True`，否则返回`False`。

```python
full()
```

如果队列是满的返回`True`，否则返回`False`。

```python
put(item, block=True, timeout=None)
```

将`item`放入队列。

* 如果可选参数`block`是`True`并且`timeout`是`None`，则阻塞至有空闲插槽可用。
* 当`timeout` 是个正数时，将最多阻塞`timeout`秒，如果在这段时间没有可用的空闲插槽，将引发`Full`异常。
* 当`block`是`False`时，如果空闲插槽立即可用，则把`item`放入队列，否则引发 `Full`异常(在这种情况下，`timeout`将被忽略)。

```python
put_nowait(item)
```

相当于 `put(item, False)` 。

```python
get(block=True, timeout=None)
```

从队列中移除并返回一个项目。

* 如果可选参数`block`是`True`并且`timeout`是`None`，则阻塞至有空闲插槽可用。
* 当`timeout`是个正数时，最多阻塞`timeout`秒，如果在这段时间内不能得到项目，将引发`Empty`异常。
* 当`block`是`False`时，如果一个项目立即可得到，则返回一个项目，否则引发`Empty`异常(在这种情况下，`timeout`将被忽略)。

```python
Queue.get_nowait()
```

相当于 `get(False)`。

```python
Queue.join()
```

阻塞至队列中所有的元素都被接收和处理完毕。

当条目添加到队列的时候，未完成任务的计数就会增加。
每当消费者线程调用`task_done()`，表示这个条目已经被回收，该条目所有工作已经完成。
未完成计数就会减少。当未完成计数降到零的时候，`join()`阻塞被解除。

```python
task_done()
```

表示前面排队的任务已经被完成，被队列的消费者线程使用。
每个`get()`被用于获取一个任务，后续调用`task_done()`告诉队列，该任务的处理已经完成。

如果当前正在`join()`阻塞，在所有条目都被处理后，将解除阻塞。

如果被调用的次数多于放入队列中的项目数量，将引发`ValueError`异常 。
