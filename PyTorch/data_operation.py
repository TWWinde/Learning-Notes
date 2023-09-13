import torch



####################################### item()#####################################################
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])
# 对整个张量进行求和
total_sum = torch.sum(x)
print(total_sum.item())  # 输出结果为 21   item()用于将一个标量张量（只有一个元素）转换为Python的标量，以便进行后续的计算或输出

######################################unsqueeze#########################################################
'''unsqueeze 是 PyTorch 中的一个函数，用于增加张量的维度。它可以在指定的维度上增加一个大小为1的维度。有一个形状为 (3, 4) 的张量 x
x = x.unsqueeze(0)x 的形状变为 (1, 3, 4)，其中第一个维度是新加的维度，大小为1'''
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])
x = x.unsqueeze(0)
print(x.shape)  # 输出结果为 torch.Size([1, 2, 3])

######################################.view()#########################################################
'''.view() 是用于改变张量形状的方法。它可以让你将一个张量重塑成新的形状，new_tensor = tensor.view(new_shape) tensor 是原始的张量，
new_shape 是你希望重塑成的新形状。new_shape 中的每个维度可以是一个整数值，也可以是 -1，表示该维度应根据其他维度的大小来自动推断。
.view(-1) 多维转化为一维张量'''
tensor = torch.randn(3, 4, 2)
print(tensor.shape)  # 输出：torch.Size([3, 4, 2])
new_tensor = tensor.view(6, 4)
print(new_tensor.shape)  # 输出：torch.Size([6, 4])

