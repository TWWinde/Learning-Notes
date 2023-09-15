import torch

input = torch.tensor([2.0, 4.0, 0.5])
###########################################
torch.arange(start=0, end=10, step=1)
sequence = torch.arange(0, 10)
# tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 是 PyTorch 中的一个函数，用于创建一个包含从 start 开始到 end 结束的一系列数字的一维张量。这个函数会生成一个序列，
# 步长为 step，包含的数值范围是 [start, end)，即包括起始值 start，但不包括结束值 end。

####################################################
# 对整个张量进行求和
total_sum = torch.sum(input)
print(total_sum.item())  # 输出结果为 11.0
# 指定维度进行求和
# 在维度 0 上求和，即对每一列进行求和
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])
sum_along_dim_0 = torch.sum(x, dim=0)
print(sum_along_dim_0)  # 输出结果为 tensor([5, 7, 9])

# 在维度 1 上求和，即对每一行进行求和
sum_along_dim_1 = torch.sum(x, dim=1)
print(sum_along_dim_1)  # 输出结果为 tensor([ 6, 15])

#####################################################
output = torch.reciprocal(input)
# 用于计算输入张量 input 中每个元素的倒数（即分数的倒数）
print(output)
# tensor([0.5000, 0.2500, 2.0000])

#####################################################
output = torch.argmax(input, dim=None, keepdim=False)
# 用于在指定的维度上找到张量中最大值的索引。
# * input: 输入张量。
# * dim: 沿着哪个维度寻找最大值。如果不指定，则在整个张量中寻找最大值。
# * keepdim: 如果为True，结果张量将保持与输入张量具有相同的维度，但在指定的维度上为1。
# 返回一个张量，其中每个元素都是在指定维度上找到的最大值的索引。
# 例如，如果有一个输入张量 input = torch.tensor([[3, 1, 4], [5, 2, 9]])，
# 则 torch.argmax(input, dim=1) 将返回一个新的张量 [2, 2]，表示在每一行中找到的最大值的索引。
# 往往用于分类任务对类别的输出

#####################################################

'''torch.max(final, 1) 是 PyTorch 中用于在张量中沿指定维度（在这里是维度1）找到最大值的函数调用。具体来说，它返回两个张量：

第一个返回值是包含每行最大值的张量。
第二个返回值是包含每行最大值的索引张量。
这种操作通常在深度学习中用于分类问题，其中模型的输出是一组类别的分数，通过找到每行最大值的索引，可以确定每个样本属于哪个类别。'''

final = torch.tensor([[0.1, 0.8, 0.4, 0.3],
                      [0.2, 0.5, 0.9, 0.6],
                      [0.7, 0.2, 0.5, 0.4]])

# 使用 torch.max 找到每行的最大值和对应的索引
max_values, max_indices = torch.max(final, 1)

print("每行的最大值：", max_values)   # tensor([0.8000, 0.9000, 0.7000])
print("每行的最大值的索引：", max_indices) #  tensor([1, 2, 0])
#####################################################

torch.bincount(input, weights=None, minlength=0)
'''''
input: 一个一维张量，包含非负整数。
weights (可选): 一个与 input 同样大小的张量，用于为每个值分配一个权重。默认为 None。
minlength (可选): 返回的张量的最小长度。如果指定，输出张量的长度将至少为 minlength，并且包含索引从0到 minlength-1 的计数。默认为 0。
'''''
input = torch.tensor([1, 2, 2, 3, 3, 3])
counts = torch.bincount(input)
print(counts)
# 输出: tensor([0, 1, 2, 3])，表示0出现0次，1出现1次，2出现2次，3出现3次