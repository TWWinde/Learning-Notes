'''Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits 
that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
统计字符串中重复的字母和数字的个数，字母不区分大小写'''''

def duplicate_count(text):
    input_string = text.lower()

    char_count = {}

    for char in input_string:

        if char.isalpha() or char.isdigit():
            char_count[char] = char_count.get(char, 0) + 1
            # 将字符 char 在字典 char_count 中的计数值增加 1。如果 char 不在字典中，它会被初始化为 0 然后增加 1。

    duplicate_count = sum(1 for count in char_count.values() if count > 1)
    # .value() 获取字典中char_count的所有值
    return duplicate_count
# 字典的应用