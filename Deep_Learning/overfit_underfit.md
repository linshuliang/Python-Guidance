# overfit and underfit

过拟合(overfit) 和 欠拟合(underfit)

## 过拟合（overfit）

Although it's often possible to achieve high accuracy on the trainint set,
what we really want is to develop models that generalized well to a testing set
(or data that have not been seen yet).

## 欠拟合 (underfit)

The opposite of overfitting is underfitting.
This an happen for a number of reasons:

* If the model is not powerful enough, is over-regularized.
  模型不够强大，正则化条件过紧。

* Simply not been trained long enough.
  训练时间不够长

This means the network has not learned the relavant patterns in the training data.

## 防止过拟合的方法

### 3.1 更多的训练数据(Get more training data)

When there are a small number of training examples,
the model sometimes learns from noises or unwanted details from training examples,
to an extent that it negatively impacts the performance of the model on new examples.
This phenomenon is known as overfitting.
It means that the model will have a difficult time generalizing on a new dataset.

To prevent overfitting, the best solution is to use more complete training data.

The data should cover the full range of inputs that the model is expected to handle.
数据集应涵盖模型应处理的各种情况的输入。

Additional data may only be useful if it covers new and interesting cases.
当且仅当额外的数据包含新的特征时，才会对模型泛化性的提高有作用。

A model trained on more complete data will naturally generalize better.
通常来说，经过更完整的数据训练出来的模型具有更好的泛化性。

### 3.2 降低网络的容量 (Reduce the capacity of network)

**可学习参数**

可学习参数的数量是由模型的层数和每层的单元数所决定的。在深度学习中，模型的可学习参数的数量通常称为模型的容量（capacity）。

Always keep this in mind: deep learning models tend to be good at fitting to the training data,
but the real challenge is generalization, not fitting.
深度学习模型往往擅长拟合训练数据，但真正的目标是泛化而不是拟合。

The simpliest way to prevent overfitting is to start with a small model.
防止过拟合最简单的方法就是用一个小模型来开始训练。

Intuitively, a model with more parameters will have more "memorizing capacity" and therefore will be able to
easily learn a dictionary-like mapping between training samples and their targets, a mapping without any generalization
power, but this would be useless when making predictions on previously unseen data.

直观地，参数越多的模型具有更强的记忆能力。
因此能以字典映射的方式来学习得到训练样本与目标的匹配关系，这种匹配不具有泛化能力，
当面对之前没见过的数据时，预测的准确率很低。

On the other hand, it the network has limited memorization resources, it will not be able to learn the mapping as easily.
To minimize its loss, it will have to learn compressed representations that have more predictive power.
At the same time, if model is too small, it will have difficulty fitting to the training data.
There is a balance between "too much capacity" and "not enough capacity".

如果模型的参数有限，则无法轻松地建立映射关系。
为了最大程度地减小 loss，它必须学习具有更强预测能力的压缩表示形式，从而得到更佳的泛化能力。
但是，如果模型太小，则模型无法建立训练数据的拟合关系。
因此，在“容量太小”和“容量太大”之间有一个平衡关系。

Unfortunately, there is no magical formula to determine the right size or architecture of your model,
You will have to experiment using a series of different architectures.

To find an appropriate model size, it's best to start with relatively few layers and parameters,
then begin increasing the size of the layers or adding new layers until you see diminishing returns on the validation loss.


### 3.3 为权重添加正则化 (add weight regularization)

Regularization contraints on the quantity and type of infomation youre model can store.
正则化项限制了模型可以存储的信息的数量和类型。

If a network can only afford to memorize a small number of patterns,
如果一个模型只能存储少量模式，

the optimization process will force it on the most prominent patterns,
which have a better chance  of generalizing well.
优化过程将会迫使它专注于最突出的模式，从而有更大的机率来提高模型的泛化能力。


#### Occam's Razor principle

Given two explanations for something, the explanation most likely to be correct is the 'simpliest' one,
the one that makes the least amount of assumptions.
最简单的解决方案通常是最佳的方案，因为简单的方案通常假设量也很小。

This also applies to the models learned by neural network:
given some training data and a network architecture, there are multiple sets of weights values (multiple models),
that coult explain the data, and simpler model re less likely to overfit than complex ones.

#### Add weight regularization

除了采用简单网路，降低网络的容量外，还可通过权重约束来降低网络的复杂性。

A common way to mitigate overfitting is to put constraints on the complexity of a network
by forcing its weights only to take small values, which makes the distribution of
weight values more 'regular', this is callled 'weight regularization'.

Weight regularization is done by adding to the loss function of the network a cost.
The cost comes in two flavors:

* L1 regularization: 根据权重的绝对值的总和来惩罚权重。
* L2 regularization: 根据权重的平方和来惩罚权重。

**附**

* L1 正则化：在依赖稀疏特征的模型中，L1 正则化有助于使不相关或几乎不相关的特征的权重刚好为0，从而将这些特征从模型中移除。
* L2 正则化：L2 正则化有助于使离群值权重接近于0，但又不恰好为0。在线性模型中，L2正则化始终可以改进泛化。

L1 Regularization pushes weights towards exactly zero encouraging a sparse model.
L2 Regularization will penalize the weights parameters without making them sparse since the penalty goes to zero for small weights.


### 3.4 Dropout

Dropout is one of the most effective and most commonly used regularization techniques for neural networks.

### 3.5 数据增强(data-augmentation)

Data augmentation takes the approach of generating more training data from existing training samples,
by augmenting the samples using random transformations that yield believable-looking images.

### 3.6 batch normalization
