#  TensorFlow .pb 模型文件

## 简介

谷歌推荐的保存模型的方式是保存模型为 PB 文件，
它具有语言独立性，可独立运行，封闭的序列化格式，
任何语言都可以解析它，
它允许其他语言和深度学习框架读取、继续训练和迁移 TensorFlow 的模型。

保存为 .pb 文件时，需要先将模型的变量转换为常量，
导致减少模型的大小，适合在移动端运行。

真正离线预测使用的时候，.pb 格式的数据能够保证数据不会更新变动，
就是不会进行反馈调节啦。