
########################################yield#######################################

''''
 是一个关键字，用于定义生成器函数。生成器函数是一种特殊类型的函数，可以用来迭代产生一系列的值，而不需要一次性将所有的值存储在内存中。
当你在函数中使用 yield 关键字时，函数将变成一个生成器函数。每次调用生成器函数时，它会执行函数体中的代码，直到遇到 yield 语句。
然后，函数会暂停执行，并将 yield 后面的值返回给调用者。生成器函数的状态会被保留，以便下次继续执行。'''''
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # 输出 1
print(next(gen))  # 输出 2
print(next(gen))  # 输出 3

########################################next()#######################################
'''''
next() 函数用于获取可迭代对象的下一个元素。
next(iterator, default)
* iterator：要获取下一个元素的可迭代对象。
* default（可选）：如果可迭代对象已经到达末尾，返回的默认值。
next() 函数在迭代过程中每次都会返回可迭代对象的下一个元素，直到可迭代对象的所有元素都被遍历完毕。如果没有提供默认值并且已经遍历到末尾，
则会触发 StopIteration 异常'''

my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

next_element = next(my_iterator)
print(next_element)  # 输出 1

next_element = next(my_iterator)
print(next_element)  # 输出 2

next_element = next(my_iterator)
print(next_element)  # 输出 3

next_element = next(my_iterator, "迭代器已结束")
print(next_element)  # 输出 "迭代器已结束"

########################################shutil.copyfile#######################################
'''
用于将一个文件的内容复制到另一个文件中。'''
import shutil
original_file_path = 'path/to/source/file.txt'
new_file_path = 'path/to/destination/file.txt'
# 复制源文件的内容到目标文件
shutil.copyfile(original_file_path, new_file_path)

########################################isinstance#######################################
'''isinstance 是一个 Python 内置函数，用于检查一个对象是否属于指定的类或类型。'''
result = isinstance(42, int)
print(result)  # 输出: True

# 检查一个字符串是否是字符串类型
result = isinstance("Hello", str)
print(result)  # 输出: True

# 检查一个列表是否是列表类型或元组类型
result = isinstance([1, 2, 3], (list, tuple))
print(result)  # 输出: True

# 检查一个对象是否是特定类的实例
class MyClass:
    pass

obj = MyClass()
result = isinstance(obj, MyClass)
print(result)  # 输出: True