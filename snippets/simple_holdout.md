### Update: 2019.10.28

### 1.简单保留验证

划分一定比例的数据作为测试数据集。

下面是比较好的实现数据集划分的代码：


```python
import glob
import os
import numpy as np
files = glob(os.path.join(path, '*/*.jpg')) # 返回结果是list
files = np.array(files) # 变成np.array类型
no_of_images = len(files)
shuffle = np.random.permutation(no_of_images) # 一个从0 ~ no_of_images - 1的随机数组
train = files[shuffle[:int(no_of_images * 0.8)]]
valida = files[shuffle[int(no_of_images * 0.8):]]
```

注意，必须是`numpy.array()`类型的数组才可能用数组作为筛选，会根据里面的数组的元素作为外层数组的下标进行选择。

上面这种划分是最简单的划分策略。

