import os

''''os.path.basename 是 Python 中的一个函数，用于从文件路径中提取文件名（即基本名称）。以下是它的基本用法：'''''
path = "/路径/到/你的/文件.txt"
filename = os.path.basename(path)
print(filename)  # 输出 文件.txt
