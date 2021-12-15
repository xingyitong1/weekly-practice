
file1 = open("111.txt","r")

content = file1.readline()

content_list1 = content.split()

num = 0

content_list2 = []
for word in content_list1:
    if num%5==0 and num !=0:
        content_list2.append("\n")
    content_list2.append(word+' ')
    num+=1
print(content_list2)

file1.close()

file2 = open("222.txt","w")

file2.writelines(word for word in content_list2)

file2.close()
        
