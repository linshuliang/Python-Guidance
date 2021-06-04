# gRPC Python 教程

## 1 定义服务

在 `.proto` 文件中定义服务（`service`）、请求(`request`)、响应(`response`)。

要定义一个`gRPC`服务，必须在 `.proto` 文件中用关键字`service`定义服务类型，例如：

```proto
// Interface exported by the server
service RouteGuide {
    // A simple RPC
    rpc GetFeature(Point) returns (Feature) {}

    // A response-streaming RPC
    rpc ListFeatures(Rectangle) returns (stream Feature) {}

    // A request-streaming RPC
    rpc RecordRoute(stream Point) return (RouteSummary) {}

    // A Bidirectional streaming RPC
    rpc RouteChat(stream RouteNote) return (stream RouteNote) {}
}
```

在 `service` 中定义`rpc`方法，指定请求和响应类型。

根据`request`和`response`前是否有关键字`stream`，`gRPC`将`service`方法分为4种方法，分别为：

| `service rpc` 方法    | 作用 |
| :------------------: | :--- |
| 简单RPC(`simple RPC`) | The **client** sends a `request` to the **server** using the `stub`(存根), waiting for a `response` to come back, just like a normal function call |
| 应答流式RPC(`response-streaming RPC`) | 在`response`前加关键字`stream`，就能指定一个`response-streaming`方法。The **client** sends a `request` the **server** and gets a return stream |
| 请求流式RPC(`request-streaming RPC`) | 在`request`前加关键字`stream`，就能指定一个`request-streaming`方法。The client writes a sequence of messages and sends them to the server. Once the **client** has finished writing the meassages, it waits for the **server** to read them all and return its response |
| 双向流式RPC(`bidirectional-streaming RPC`) | 一个 双向流式 RPC 是双方使用读写流去发送一个消息序列。两个流独立操作，因此客户端和服务器可以以任意喜欢的顺序读写：比如， 服务器可以在写入响应前等待接收所有的客户端消息，或者可以交替的读取和写入消息，或者其他读写的组合。 每个流中的消息顺序被预留 |

## 2 创建服务器

```python
class RouteGuideServicer(route_guide_pb2_grpc.RouteGuideServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        self.db = route_guide_resources.read_route_guide_database()
```

### 2.1 simple RPC

```python
def GetFeature(self, request, context):
    feature = get_feature(self.db, request)
    if feature is None:
        return route_guide_pb2.Feature(name="", location=request)
    else:
        return feature
```

请求`request`和响应`response`都是一个对象。

### 2.2 response-streaming RPC

```python
def ListFeatures(self, request, context):
    """生成器
    """
    left = min(request.lo.longitude, request.hi.longitude)
    right = max(request.lo.longitude, request.hi.longitude)
    top = max(request.lo.latitude, request.hi.latitude)
    bottom = min(request.lo.latitude, request.hi.latitude)
    for feature in self.db:
        if (feature.location.longitude >= left and
                feature.location.longitude <= right and
                feature.location.latitude >= bottom and
                feature.location.latitude <= top):
            yield feature
```

请求`request`是一个对象，响应`response`是一个可迭代对象(`Iterable Object`)。

### 2.3 request-streaming RPC

```python
def RecordRoute(self, request_iterator, context):
    point_count = 0
    feature_count = 0
    distance = 0.0
    prev_point = None

    start_time = time.time()
    for point in request_iterator:
        point_count += 1
        if get_feature(self.db, point):
            feature_count += 1
        if prev_point:
            distance += get_distance(prev_point, point)
        prev_point = point

    elapsed_time = time.time() - start_time
    return route_guide_pb2.RouteSummary(point_count=point_count,
                                        feature_count=feature_count,
                                        distance=int(distance),
                                        elapsed_time=int(elapsed_time))
```

请求`request`是一个可迭代对象(Iterable Object)，响应`response`是一个对象。

### 2.4 bidirectional-straming RPC

```python
def RouteChat(self, request_iterator, context):
    prev_notes = []
    for new_note in request_iterator:
        for prev_note in prev_notes:
            if prev_note.location == new_note.location:
                yield prev_note
        prev_notes.append(new_note)
```

请求`request`和响应`response`都是可迭代对象(Iterable Object)。

## 3 创建客户端

对于返回单个应答的 RPC 方法，gRPC Python 同时支持同步（阻塞）和异步（非阻塞）的控制流语义。

### 3.1 simple RPC

同步调用 **simple RPC** `GetFeature` 几乎是和调用一个本地方法一样直观。
RPC 调用等待服务器应答，它要么返回应答，要么引起异常：

```python
feature = stub.GetFeature(point, timeout_in_seconds)
```

GetFeature 的异步调用很类似，但和在一个线程池里异步调用一个本地方法很像：

```python
feature_future = stub.GetFeature.future(point, timeout_in_seconds)
feature = feature_future.result()
```

### 3.2 response-streaming RPC

对于 **response-streaming RPC** 方法，调用会立即返回一个应答值的迭代器。
调用迭代器的 `next()` 方法会阻塞，直到从迭代器产生的应答变得可用。

调用应答流 `ListFeatures` 和使用序列类型类似：

```python
for feature in stub.ListFeatures(rectangle, timeout_in_seconds):
```

### 3.3 request-streaming RPC

调用 **request-streaming RPC** `RecordRoute` 和给一个本地方法传入序列类似。
和前面的简单 RPC 一样，它也会返回单个应答，可以被同步或者异步调用：

```python
route_summary = stub.RecordRoute(point_sequence, timeout_in_seconds)
route_summary_future = stub.RecordRoute.future(point_sequence, timeout_in_seconds)
route_summary = route_summary_future.result()
```

### 3.4 bidirectional RPC

调用**bidirectional RPC** `RouteChat` 是请求流和应答流语义的结合（这个场景是在服务器端）。

```python
for received_route_note in stub.RouteChat(sent_routes, timeout_in_seconds):
```

## 参考

* [gRPC 官方中文文档](http://doc.oschina.net/grpc?t=60138)
* [gRPC Python Basic Tutorial](https://grpc.io/docs/languages/python/basics/)
