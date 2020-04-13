# numpy

## 创建一个 ndarray

| API | 功能  |
|:----| :-----|
|[np.linspace](create_ndarray/numpy.linspace.py)| 创建一个数组，元素为给定区间中均匀间隔的数字 |
|[np.arange](create_ndarray/numpy.arange.py)| 创建一个数组，元素为给定区间中均匀间隔的数字，一般只用于整数 |
|[np.empty](create_ndarray/numpy.empty.py)| 创建一个未初始化的数组 |
|[np.zeros](create_ndarray/numpy.zeros.py)| 创建一个数组，元素全为0 |
|[np.ones](create_ndarray/numpy.ones.py)| 创建一个数组，元素全为1 |
|[np.full](create_ndarray/numpy.full.py)| 创建一个数组，元素全为给定值 |
|np.empty\_like| 给定一个数组x，np.empty\_like(x) 会创建一个形状相同的未初始化的数组 |
|[np.zeros\_like](create_ndarray/numpy.zeros_like.py)| 给定一个数组x，np.zeros\_like(x) 会创建一个形状相同的全0数组 |
|[np.ones\_like](create_ndarray/numpy.ones_like.py)| 给定一个数组x，np.ones\_like(x) 会创建一个形状相同的全1数组 |
|np.full\_like| 给定一个数组x，np.full\_like(x) 会创建一个形状相同的数组，元素为给定值 |


## numpy 数学函数

| API | 功能  |
|:----| :-----|
|[np.clip](math/numpy.clip.py) | 将ndarray 的值限定于[`a_min`， `a_max`] |
|[np.sort](math/numpy.sort.py) | 数组排序 |
|[np.floor](math/numpy.floor.py)| 数组向下取整 |

## 基础API

| API | 功能  |
|:----| :-----|
|[ndarray.T](ndarray.T.py)| 将一个数组转置 |
|[np.copy](numpy.copy.py) | 深拷贝一个 ndarray |
|[ndarray.copy](ndarray.copy.py) | 深拷贝一个 ndarray |
|[np.save and np.load](numpy.save_numpy.load.py) | ndarray 的保存与加载 |

## 改变数组的形状

| API | 功能  |
|:----| :-----|
|[np.stack](shape_manipulation/numpy.stack.py) | 堆叠数组 |
|[np.squeeze](shape_manipulation/numpy.squeeze.py) | 删除数组中维度是1的条目 |
|[np.reshape](shape_manipulation/numpy.reshape.py) | 改变 ndarray 的形状 |
|[np.expand\_dims](shape_manipulation/numpy.expand_dims.py) | 在不改变 ndarray 的数值下，新增维度 |

## np.random

| API | 功能  |
|:----| :-----|
|[np.random.rand](numpy.random/numpy.random.rand.py) | 生成一个随机数组，均匀分布，`[0, 1]`之间 |
