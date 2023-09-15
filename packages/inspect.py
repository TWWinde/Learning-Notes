
import inspect
'''inspect.signature 是 Python 标准库中 inspect 模块中的一个函数，用于获取函数的签名信息，包括参数、参数类型、默认值等。
函数签名描述了函数的形式参数及其特征。'''''
def example_function(a, b=10, *args, **kwargs):
    pass

# 获取函数签名
signature = inspect.signature(example_function)

# 打印函数签名
print('Parameters:', list(signature.parameters))
print('Return annotation:', signature.return_annotation)

# 获取参数的详细信息
for param_name, param in signature.parameters.items():
    print('Parameter:', param_name)
    print('  - Default value:', param.default)
    print('  - Annotation:', param.annotation)
    print('  - Kind:', param.kind)
    print('  - Is positional:', param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD)
    print('  - Is required:', param.default == inspect.Parameter.empty)
