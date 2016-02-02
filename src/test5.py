
# 用字典表达映射关系
empty_dict = {}
# 初始化的字典
filled_dict = {"one": 1, "two": 2, "three": 3}

# 用[]取值
print(filled_dict["one"])   # => 1


our_iterable = filled_dict.keys()
print(our_iterable)
for i in our_iterable:
    print(i)


list(filled_dict.keys())
print(list)
