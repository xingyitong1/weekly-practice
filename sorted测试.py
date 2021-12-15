aStr = '27 56 4 18'
aStr_aList = list(aStr)
print('aStr_aList is', aStr_aList)

aList = aStr.split()
aList.sort()
print('aList排好序为：', aList)

##
##
bStr = ' '.join(aList)
print('bStr is', bStr)

##
##
##
test1List = [27, 56, 4, 18]
cList = sorted(test1List)
print('使用sorted对列表test1ListcList排序后产生新列表cList为', cList)
test1List.sort()                      ##sort只能用于列表
print(test1List)

##
##
##
test1Str = '27, 56, 4, 18'          ##sorted可用于字符串
StrSorted = sorted(test1Str)
print('StrSorted对字符串排序结果：', StrSorted)


##
test2Str = '27 56 4 18'
StrSorted2 = sorted(test2Str)
print('StrSorted2 is', StrSorted2)

##
##
test3Str = 'Hello World'
StrSorted3 = sorted(test3Str)
print('StrSorted3 is', StrSorted3)
