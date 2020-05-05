# Estimator

Estimators use a system called feature columns to describe how the model should interpret each of the raw input features.
Estimator 使用一个名为 `feature columns` 的系统来描述，模型应该如何解释每个原始输入特征。

An Estimator expects a vector of numeric inputs, and feature columns describe how the model should convert each feature.
一个 Estimator 需要一个数字输入向量，feature columns 描述了模型如何转换每个特征。

Selecting and crafting the right set of feature columns is key to learning an effective model.
选择和制作正确的 `feature columns` 是学习一个有效模型的关键。

A feature column can be either one of the raw inputs in the original feature dict (a base feature column),
一个 feature column 既可以是原始特征字典的原始输入之一（称为基本特征列），

or any new columns created using transformations defined over one or multiple base columns (a derived feature columns).
也可以是在一个或多个基本特征列上变换得到的新的特征列 （称为派生特征列）。
