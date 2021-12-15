import copy

Given_x = [1,2,3]

copylist_x = copy.copy(Given_x)

#不可变的y列表
immutable_y = copy.copy(Given_x)
#可变列表y
mutable_y = Given_x

print("原可变列表y是",mutable_y)

print("原不可变y列表是",immutable_y)

#改变x列表的其中一个值
Given_x[1] = 5
print("改变了x列表中的一个值")

print("现不可变y列表是",immutable_y)
print("现可变y列表是",mutable_y)


