import torch
import torch.nn.functional as F

# 定义网络类
class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    # 重写此函数，前向传播
    def forward(self, x):
        x = F.sigmoid(self.hidden(x))
        x = self.predict(x)
        out = F.log_softmax(x.dim=1)
        return out

# 实例化网络
