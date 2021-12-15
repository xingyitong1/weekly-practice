#全部为整数类型的
Given_list_int = [1,2,3,4]
#将元素全部换成字符串类型，否则无法连接
Given_list_str = []
for i in Given_list_int:
    Given_list_str.append(str(i))
    
string_list = ''.join(Given_list_str)


print(string_list)
