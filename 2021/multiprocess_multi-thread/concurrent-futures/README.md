# concureent.futures - 启动并行任务

## 1 简介

`concurrent.futures` 模块提供异步执行可调用对象的高层接口。

异步执行的实现方法:

* `ThreadPoolExecutor` 使用线程池
* `ProcessPoolExecutor` 使用单独的进程池

`ThreadPoolExecutor` 和 `ProcessPoolExecutor` 都由抽象类 `Executor` 派生而来。

## 2 Executor 对象

抽象类`Executor`提供异步执行调用方法。

```python
submit(fn, *args, **kwargs)
```

执行可调用对象`fn`，以`fn(*args, **kwargs)`方式执行，并返回`Future`对象代表可调用对象的执行。

```python
map(func, *iterables, timeout=None, chunksize=1)
```

返回结果等同于 `map(func, iterables)`，但以异步方式执行。

```python
shutdown(wait=True)
```

清理与`Executor`相关联的资源。

## 3 Future 对象

`Future`类将可调用对象封装为异步执行，`Future`实例由`Executor.submit()`创建。

```python
result(timeout=None)
```

返回调用的结果。

## 4 ThreadPoolExecutor

```python
class concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix='')
```

`Executor`子类`ThreadPoolExecutor`使用最多`max_workers`个线程的线程池来异步执行调用。

示例：

```python
# coding=utf-8
import concurrent.futures
import urllib.request


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    URLS = ['https://translate.google.cn/',
            'https://www.google.com']
    future_to_url = {}
    for url in URLS:
        future = executor.submit(load_url, url, 60)
        future_to_url[future] = url

    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print("%r generated an exception: %s" % (url, exc))
        else:
            print("%r page is %d bytes" % (url, len(data)))
```

## 5 ProcessPoolExecutor

```python
class concurrent.futures.ProcessPoolExecutor(max_workers=None)
```

使用进程池来实现异步执行调用。

示例：

```python
# coding=utf-8
import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n : int) -> bool :
    if n > 2 and n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False

    return True

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print("%d is prime: %s" % (number, prime)
```
