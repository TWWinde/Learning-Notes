

'''''''.get() 是一个通用的方法，它可以应用于各种不同的数据结构和对象，具体行为取决于该对象的类型。通常，.get() 用于获取对象的属性、元素或值。'''

my_dict = {'key1': 'value1', 'key2': 'value2'}
value = my_dict.get('key1')
print(value)  # 输出: 'value1'
# .get()用来获取字典中某个键对应的值



'''''''del 是一个Python关键字，用于删除变量、对象或对象中的属性。'''''''
x = 10
del x  # 删除变量x
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # 删除索引为2的元素，列表变为 [1, 2, 4, 5]


'''.keys() 方法通常用于获取字典（dictionary）中的所有键（keys），返回一个包含所有键的可迭代对象（通常是一个列表或类似列表的数据结构）。
这个方法允许你迭代字典中的键或者检查某个特定键是否存在于字典中。'''
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# 获取字典中所有键
keys = my_dict.keys()
# 打印所有键
for key in keys:
    print(key)   # 'name' , 'age', 'city'

'''''''如何取两个list的交集'''''''
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = list(set(list1) & set(list2))
intersection1 = [value for value in list1 if value in list2]
intersection2 = list(filter(lambda value: value in list2, list1))