----

Time: 201980725

Author: BING

----

## 关于PyTorch使用的一些小抄。

### nn.Module下的`forward`函数

这是一个必须实现的函数，用于表示张量在网络中的流动，决定了网络的结构。

参考：https://www.cnblogs.com/ziytong/p/10677771.html

### nn.Conv2d

### 数据处理

可以先用标准的Python包将数据加载为Numpy数组，再转成PyTorch的张量。

- images ==> Pillow, OpenCV
- audio ==> scipy, librosa
- text ==> Python基础加载方式，或NLTK，SpaCy

特别针对视觉相关任务，开发了`torchvision`包。两个基础包：

- `torchvision.datasets`
- `torchvision.utils.data.DataLoader`



