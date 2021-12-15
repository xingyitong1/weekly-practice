L = [1,2,3]
print(L, 'id:', id(L))

L = L + [9]
print(L, 'id:', id(L))   # 创建了新对象

L.append(9)
print(L, 'id:', id(L))   # 未创建新对象
