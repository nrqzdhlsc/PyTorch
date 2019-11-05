import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision 
import torchvision.transforms as transforms

from alexnet_v2 import AlexNet

# 目标：加载CIFAR10，训练AlexNet
# 准备数据集
train_set = torchvision.datasets.CIFAR10(
    root='./data/CIFAR10',
    download=True,
    train=True,
    transform=transforms.Compose(
        [transforms.ToTensor()]
    )
)

network = AlexNet() 

train_data_loader = torch.utils.data.DataLoader(train_set, batch_size=100)
optimizer = optim.Adam(network.parameters(), lr=0.01)

# batch = next(iter(train_data_loader)) # 
# images, labels = batch
# print(images[0].unsqueeze(dim=0).shape) # [3, 32, 32]

# 训练多个epochs
epochs = 10
total_loss = 0.0
for i in range(epochs):
    for batch in train_data_loader:
        images, labels = batch
        preds = network(images)
        loss = F.cross_entropy(preds, labels)  # 计算损失函数

        # BP前需要先将梯度置为0
        optimizer.zero_grad()
        loss.backward()  # 计算梯度
        optimizer.step()  # 一个批次更新参数
        total_loss += loss.item()

    print("current loss in sum: ", total_loss)


