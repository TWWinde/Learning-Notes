

'''''''.get() 是一个通用的方法，它可以应用于各种不同的数据结构和对象，具体行为取决于该对象的类型。通常，.get() 用于获取对象的属性、元素或值。'''

my_dict = {'key1': 'value1', 'key2': 'value2'}
value = my_dict.get('key1')
print(value)  # 输出: 'value1'


'''''''del 是一个Python关键字，用于删除变量、对象或对象中的属性。'''''''
x = 10
del x  # 删除变量x
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # 删除索引为2的元素，列表变为 [1, 2, 4, 5]