# 组织列表
# 相关函数: 顺序sort(), 顺序临时sorted(), 反序reverse().
# 下面创建列表, 来灵活运用三种排列函数.

# 首先'创建一个排序杂乱的列表',并'打印'将其显示
print('--------------[Creat a new list]--------------')
List_count = ['4', '2', '1', '5', '3']
print(List_count)
print('----------------------------------------------\n')

# 在'未修改列表'内容的情况下'打印排序好的列表'.
print('------------------[sorted]--------------------')
print('Here is the oringinal list:      ', List_count)
print('Here is the sorted list:         ', sorted(List_count))
print('Here is the oringinal list again:', List_count)
print('----------------------------------------------\n')

# 使用sorted()按与字母相反的顺序排列并打印,同时不要修改它
print('-------------[sorted and reverse]-------------')
print('Here is the oringinal list:        ', List_count)
print('Here is the sorted and revere list:', sorted(List_count, reverse=True))
print('Here is the oringinal list again:  ', List_count)
print('----------------------------------------------')

# 使用sort正序排序列表, 打印核实列表顺序改变, 再度重复此操作.
print('--------------[sort and reverse]--------------')
print('Here is the oringinal list:    ', List_count)
List_count.sort()
print('Here is the sort list:         ', List_count)
List_count.sort(reverse=True)
print('Here is the reverse list again:', List_count)
print('----------------------------------------------\n')
