import torch



# item()
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])
# 对整个张量进行求和
total_sum = torch.sum(x)
print(total_sum.item())  # 输出结果为 21   item()用于将一个标量张量（只有一个元素）转换为Python的标量，以便进行后续的计算或输出
