import os

file_name1 = input("输入第一个文件的名字")
file_name2 = input("输入第二个文件的名字")


while not os.path.isfile(file_name1):
    file_name1 = input("输入第一个文件的名字")
 
while not os.path.isfile(file_name2):
    file_name2 = input("输入第二个文件的名字")


first_file = open(file_name1,"r")
second_file = open(file_name2,"r")

content1 = ''
for line_str1 in first_file:
    content1+=(line_str1)
print(content1)

content2 = ''
for line_str2 in second_file:
    content2+=line_str2
print(content2)

first_file.close()
second_file.close()

first_file = open(file_name1,"w")
second_file = open(file_name2,"w")


first_file.write(content2)
second_file.write(content1)

first_file.close()
second_file.close()
