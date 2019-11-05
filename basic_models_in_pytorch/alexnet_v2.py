import torch
import torch.nn as nn
import torch.nn.functional as F

class AlexNet(nn.Module):
    def __init__(self, num_classes=1000):
        super(AlexNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, 
                    kernel_size=11, stride=4, padding=2)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=192, 
                    kernel_size=5, padding=2)
        self.conv3 = nn.Conv2d(in_channels=192, out_channels=384,
                    kernel_size=3, padding=1)
        self.conv4 = nn.Conv2d(in_channels=384, out_channels=256, 
                    kernel_size=3, padding=1)
        self.conv5 = nn.Conv2d(in_channels=256, out_channels=256, 
                    kernel_size=3, padding=1)
        self.avgpool = nn.AdaptiveAvgPool2d((6, 6))

        self.fc1 = nn.Linear(in_features=256*6*6, out_features=4096)
        self.fc2 = nn.Linear(in_features=4096, out_features=4096)
        self.fc3 = nn.Linear(in_features=4096, out_features=num_classes)

    def forward(self, t):
        # 组装张量处理操作
        t = self.conv1(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=3, stride=2)

        t = self.conv2(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=3, stride=2)

        t = self.conv3(t)
        t = F.relu(t)

        t = self.conv4(t)
        t = F.relu(t)

        t = self.conv5(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=3, stride=2)

        t = self.avgpool(t)
        
        # 将最后输出的特征图展平
        t = torch.flatten(t)
        # 开始接分类器操作
        t = F.dropout2d(t)
        t = self.fc1(t)
        t = F.relu(t)
        t = F.dropout2d(t)
        t = self.fc2(t)
        t = F.relu(t)
        t = self.fc3(t)

        return t





