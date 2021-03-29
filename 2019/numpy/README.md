# numpy

## array creation

| API | 功能  |
|:----| :-----|
|[np.linspace](array_creation/numpy.linspace.py)| 创建一个数组，元素为给定区间中均匀间隔的数字 |
|[np.arange](array_creation/numpy.arange.py)| 创建一个数组，元素为给定区间中均匀间隔的数字，一般只用于整数 |
|[np.empty](array_creation/numpy.empty.py)| 创建一个未初始化的数组 |
|[np.zeros](array_creation/numpy.zeros.py)| 创建一个数组，元素全为0 |
|[np.ones](array_creation/numpy.ones.py)| 创建一个数组，元素全为1 |
|[np.full](array_creation/numpy.full.py)| 创建一个数组，元素全为给定值 |
|np.empty\_like| 给定一个数组x，np.empty\_like(x) 会创建一个形状相同的未初始化的数组 |
|[np.zeros\_like](array_creation/numpy.zeros_like.py)| 给定一个数组x，np.zeros\_like(x) 会创建一个形状相同的全0数组 |
|[np.ones\_like](array_creation/numpy.ones_like.py)| 给定一个数组x，np.ones\_like(x) 会创建一个形状相同的全1数组 |
|np.full\_like| 给定一个数组x，np.full\_like(x) 会创建一个形状相同的数组，元素为给定值 |
|[np.copy](array_creation/numpy.copy.py) | 深拷贝一个 ndarray |
|[ndarray.copy](array_creation/ndarray.copy.py) | 深拷贝一个 ndarray |

## numpy 数学函数

| API | 功能  |
|:----| :-----|
|[np.clip](math/numpy.clip.py) | 将ndarray 的值限定于[`a_min`， `a_max`] |
|[np.floor](math/numpy.floor.py)| 数组向下取整 |

## 基础API

| API | 功能  |
|:----| :-----|
|[ndarray.T](ndarray.T.py)| 将一个数组转置 |
|[np.save and np.load](numpy.save_numpy.load.py) | ndarray 的保存与加载 |

## ordering

| API | 功能  |
|:----| :-----|
|[np.sort](ordering/numpy.sort.py) | 数组排序 |
|[np.argsort](ordering/numpy.argsort.py) | 返回数组排序后的位置列表  |
|[np.argmin](ordering/numpy.argmin.py) | 返回沿轴axis 的最小值的索引 |
|[np.argmax](ordering/numpy.argmax.py) | 返回沿轴axis 的最大值的索引 |
|[np.min](ordering/numpy.min.py) | 返回沿轴 axis 的最小值 |
|[np.max](ordering/numpy.max.py) | 返回沿轴 axis 的最大值 |

## 改变数组的形状

* split : Split array into a list of multiple sub-arrays of equal size.
* hsplit : Split array into multiple sub-arrays horizontally (column wise)
* vsplit : Split array into multiple sub-arrays vertically (row wise)
* stack : Stack a sequence of arrays along a new axis.
* hstack : Stack arrays in sequence horizontally (column wise)
* vstack : Stack arrays in sequence vertically (row wise)

| API | 功能  |
|:----| :-----|
|[np.squeeze](shape_manipulation/numpy.squeeze.py) | 删除数组中维度是1的条目 |
|[np.reshape](shape_manipulation/numpy.reshape.py) | 改变 ndarray 的形状 |
|[np.expand\_dims](shape_manipulation/numpy.expand_dims.py) | 在不改变 ndarray 的数值下，新增维度 |
|[np.stack](shape_manipulation/numpy.stack.py) | 堆叠数组 |
|[np.hstack](shape_manipulation/numpy.hstack.py) | 沿着水平方向将数组堆叠起来，按列合并 |
|[np.vstack](shape_manipulation/numpy.vstack.py) | 沿着竖直方向将数组堆叠起来，按行合并。 np.vstack((a, b)) 等同于 np.concatenate((a, b)) |
|[np.concatenate](shape_manipulation/numpy.concatenate.py) | 沿着一条现有的轴，来连接一系列数组 |

## np.random

| API | 功能  |
|:----| :-----|
|[np.random.rand](numpy.random/numpy.random.rand.py) | 生成一个随机数组，均匀分布，`[0, 1]`之间 |
