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