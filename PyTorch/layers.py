import torch
from torch import nn


#########################################nn.Conv2d############################################
conv_layer = torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=0, dilation=1, groups=1,
                             bias=True, padding_mode='zeros')
# * in_channels：输入数据的通道数（输入特征图的深度）。
# * out_channels：输出数据的通道数（输出特征图的深度）。
# * kernel_size：卷积核的大小，可以是一个整数表示正方形核的边长，或者是一个元组 (h, w) 表示核的高度和宽度。
# * stride：卷积核的步幅，默认为 1。
# * padding：输入数据的边缘补零大小，可以是一个整数或一个元组，用于控制输出特征图的大小。
# * dilation：卷积核的扩张大小，用于控制卷积核的感受野。
# * groups：控制输入和输出通道之间的连接方式，默认为 1，表示普通的卷积操作，如果大于 1，表示使用分组卷积。
# * bias：是否使用偏置项，默认为 True。
# * padding_mode：边缘填充方式，默认为 'zeros'，可以是 'zeros'、'reflect'、'replicate' 或 'circular'

#########################################torch.nn.Identity()#######################################
torch.nn.Identity()
# 是 PyTorch 中的一个简单的恒等（identity）模块，用于将输入不经过任何改变地输出。这在构建神经网络时可能会用到，
# 特别是在需要将某个特征或张量传递到下一层时，但不需要进行任何转换或操作。
identity = nn.Identity()
x = torch.tensor([1.0, 2.0, 3.0])
y = identity(x)
print(y)  # 输出结果为 tensor([1., 2., 3.])



#########################################nn.ModuleList#######################################
ModuleList = nn.ModuleList
'''是PyTorch中的一个模块，用于包含多个子模块的列表。它类似于Python的标准列表，但被设计用于存储PyTorch的模块，
这些模块可以在神经网络中作为子模块使用。使用nn.ModuleList可以方便地管理和追踪一系列子模块。'''

class MyModule(nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()
        self.module_list = nn.ModuleList([
            nn.Linear(10, 20),
            nn.ReLU(),
            nn.Linear(20, 30),
            nn.ReLU()
        ])

    def forward(self, x):
        for layer in self.module_list:
            x = layer(x)
        return x
