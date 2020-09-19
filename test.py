# 测试1：字典的键序列和列表的转换
# dct = {'a': 9, 'p': 2, 'e': 9, 'o': 2, 'f': 1, 'k': 2, 'w': 7, 'g': 6}
# lst = list()
# lst = dct.keys()
# lst = list(lst)
# print(lst)
#

dct = {'a': 9, 'p': 2, 'e': 9, 'o': 2, 'f': 1, 'k': 2, 'w': 7, 'g': 6}
# lst = list()
# lst = list(dct)
# print(list(dct.values()))
# print(lst)
# print(len(dct))
keylst = dct.keys()
keylst = list(keylst)
print(keylst)
# print(list(keylst))
# print(keylst)
# print(type(keylst))
'''
dict  
    键 值
    {'a':2, 'b':true}
list 
    [1, true, 'avc', [1, 2, 3], {'a':2, 'b':[1, 2, 3]}]
    
bool a[100];
'''