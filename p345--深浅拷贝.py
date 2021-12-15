aList = [1,2,3]
print('aList is', aList,'aList: ID', id(aList))
for x in aList:
    print(id(x))

print()
bList = [5,6,7]
print('bList is', bList,'bList: ID', id(bList))
aList.append(bList)
print('aList is', aList,'aList: ID', id(aList))
print('---------------------------------------')
import copy

print()

copyList = copy.copy(aList)  #浅拷贝
print('copyList (浅拷贝) is', copyList,'copyList: ID', id(copyList))
for x in copyList:
    print(id(x))
print('**************************************')
print()


lightCopyList = aList[:]   #浅拷贝

print('lightCopyList (浅拷贝) is', lightCopyList,'lightCopyList: ID', id(lightCopyList))
for x in lightCopyList:
    print(id(x))

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print()
deepCopyList = copy.deepcopy(aList)  #深拷贝
print('deepCopyList (深拷贝) is', deepCopyList,'deepCopyList: ID', id(deepCopyList))
for x in deepCopyList:
    print(id(x))
print("马上修改a中第一个元素值！")
aList[0] = 'aa'     #修改a第一层值不会影响浅拷贝
print('aList', aList,'aList: ID', id(aList))
print('aList中的各个元素id值：')
for x in aList:
    print(id(x))
print()
print('deepCopyList中的各个元素及其id值：')
for x in deepCopyList:
    print(x,id(x))
print('………………………………………………')
print("深拷贝不受影响！保持原值")
print()


print('copyList (浅拷贝)', copyList,'copyList: ID', id(copyList))
for x in copyList:
    print(id(x))
print("浅拷贝也不受影响！保持原值")
print()

bList[0] = 1000

print("$$$$$$$$$$$$$$$$$$我是华丽分割线$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print('bList', bList,'bList: ID', id(bList))

print('copyList (浅拷贝)', copyList,'copyList: ID', id(copyList))
for x in copyList:
    print(id(x))
print("浅拷贝此时受影响了")


print()
print('lightCopyList (浅拷贝)', lightCopyList,'lightCopyList: ID', id(lightCopyList))
for x in lightCopyList:
    print(id(x))
print()


print('deepCopyList(深拷贝)', deepCopyList,'deepCopyList: ID', id(deepCopyList))
for x in deepCopyList:
    print(id(x))
print("修改下一层，深拷贝仍然不受影响")




####可变与不可变
##
##L = [1,2,3]
##print(L, 'id:', id(L))
##
##L = L + [9]
##print(L, 'id:', id(L))   # 创建了新对象
##
##L.append(9)
##print(L, 'id:', id(L))   # 未创建新对象

