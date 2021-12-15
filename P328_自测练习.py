myList = [1.6,2.7,3.8,4.9]
newList=[]
newList2=[]
aList=[]

for val in myList:
    temp = str(val)
    aList.append(temp.split('.'))

for val in aList:
    newList.append(int(val[0]))
    newList2.append(int(val[1]))

myStr = '：'.join(val)


print('myLsit',myList)
print('aList',aList)
print('newList',newList)
print('newList2',newList2)
print('val',val)
print('myStr',myStr)
