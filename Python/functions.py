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
'''isinstance 是一个 Python 内置函数，用于检查一个对象是否属于指定的类或类型。   '''
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

######################################## map() #######################################
'''''
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
map(function, iterable, ...)'''

def square(x):
    return x ** 2

list(map(square, [1,2,3,4,5])) # get [1, 4, 9, 16, 25]
list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]) ) # get [1, 4, 9, 16, 25]
list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))  # get [3, 7, 11, 15, 19]

########################################zip()#######################################
'''''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
我们可以使用 list() 转换来输出列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。'''

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 返回一个对象<zip object at 0x103abc288>

list(zipped)  # list() 转换为列表[(1, 4), (2, 5), (3, 6)]
list(zip(a,c))   # 元素个数与最短的列表一致[(1, 4), (2, 5), (3, 6)]

a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
list(a1) # [1, 2, 3]
list(a2) # [4, 5, 6]
