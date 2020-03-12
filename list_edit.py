#  ----------------------------------------------
# | Build in 2020.03.09 22:00 - 2020.03.10 2:00  |
# | Tester:KaryoYou                              |
#  ----------------------------------------------
#
# 创建列表,包含3个元素,并使用这个列表打印消息.
Guests = ['aa', 'bb', 'cc']
# 定义消息内容;由于消息内容过长,使用 \ 符号进行换行编辑; 建议代码行长度为 80 以内.
message = "Hi: " + \
          Guests[0].title() + ", " + \
          Guests[1].title() + " and " + \
          Guests[2].title() + ". " + \
          "Would you like to join my dinner tonight?\n"
# 打印消息
print(message)

# 修改列表元素
# 重新定义消息内容, 调用列表引索为 1 的元素, 并将消息打印出来;
message = "Sorry guy, " + \
          Guests[1].title() + \
          " is busy, he cant join to us.\n"
print(message)

# 重新赋值列表引索为 1 的元素
Guests[1] = 'dd'
# 重新定义消息内容, 调用列表引索为 1 的元素, 并将消息打印出来;
message = "But " + Guests[1].title() + " will be come in.\n"
print(message)

# 使用 append() 添加列表元素; 所添加的元素会位于列表的最后一个.
Guests.append('ee')
Guests.append('ff')
Guests.append('gg')
# 重新定义消息内容, 引用列表元素编辑并打印消息
message = "Everybody, I find a place is bigger, I want to get there.\n"
print(message)

# 使用 insert(整数, '元素值') 插入元素到列表开头.
# insert()中的整数即插入位的引索值, ''内为元素值.
Guests.insert(0, 'hh')
# 使用 insert() 插入元素到列表中间.
Guests.insert(3, 'ii')
# 使用 append() 在列表末端添加元素.
Guests.append('jj')
# 由于列表元素太多, 暂将列表打印出来, 数数个数. (后期应该会学到获得列表长度的函数)
# print("Guests list:", Guests, "\n")
# 由打印结果得知列表一共有 9 个元素, 调用列表元素打印消息
message = "Hi: " + \
          Guests[0].title() + ", " + \
          Guests[1].title() + ", " + \
          Guests[2].title() + ", " + \
          Guests[3].title() + ", " + \
          Guests[4].title() + ", " + \
          Guests[5].title() + ", " + \
          Guests[6].title() + ", " + \
          Guests[7].title() + " and " + \
          Guests[8].title() + ". " + \
          "do you follow ?\n"
print(message)

# 编辑并打印一条消息
message = "Sorry everybody, just now i get a message.\n" + \
          "The new table haven't arrived on the time.\n" + \
          "So just two guy can join dinner in tonight.\n"
print(message)

# 删除列表元素, 删至剩余两位后, 每次删除元素都打印列表
# 删除方法1: del ,根据引索删除元素,删除后无法接续调用该元素
del_name = Guests[1]
del Guests[1]
print("So sorry about that, Next time i will call you, ",
      del_name.title(), " !\n")
# 删除方法2: remove() ,根据值删除元素,删除后无法接续调用该元素
remove_name = 'dd'
Guests.remove(remove_name)
print("So sorry about that, Next time i will call you, ",
      remove_name.title(), " !\n")
# 删除方法3: pop() ,根据引索删除元素,元素删除后仍可暂时调用.
pop_name = Guests.pop()  # 无参数时,删除列表最后一个元素;
print("So sorry about that, Next time i will call you, ",
      pop_name.title(), " !\n")
pop_name = Guests.pop(1)  # 有参数时,删除该引索所在元素.
print("So sorry about that, Next time i will call you, ",
      pop_name.title(), " !\n")
pop_name = Guests.pop(1)
print("So sorry about that, Next time i will call you, ",
      pop_name.title(), " !\n")
pop_name = Guests.pop(1)
print("So sorry about that, Next time i will call you, ",
      pop_name.title(), " !\n")
pop_name = Guests.pop(1)
print("So sorry about that, Next time i will call you, ",
      pop_name.title(), " !\n")
# 调用列表中剩下的两个元素并分别打印信息
print("Hey, ", Guests[0].title(),
      " you also can come. i am waiting for you.\n")
print("Hey, ", Guests[1].title(),
      " you also can come. i am waiting for you.\n")

# 使用 del 删除列表中剩余元素, 最后打印列表核实程序结束时列表是空的.
del Guests[0]
del Guests[0]
print("现在的列表内容为:", Guests)
