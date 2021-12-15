import copy
aList = [1,2,3]
bList = [5,6,7]

aList.append(bList)

print('原始：', aList)

shallowCopyList = aList[:]

deepCopyList = copy.deepcopy(aList)

aList.append(888)

bList.append(99)

aList[2] = 1111
bList[0] = 3333

print('aList追加数据后:{}'.format(aList))
print('shallowCopyList:{}'.format(shallowCopyList))
print('deepCopyList:{}'.format(deepCopyList))
