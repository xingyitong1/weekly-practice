#将文件转化为字典
def file_to_dict(file,dict):
    """将文件转化为字典"""
    reader = csv.reader(file)
    file_list = [row for row in reader]
    for row in file_list:
        dict[row[0]] = row[:5]
    print(dict)

#查找函数
def inqury(name,dict):
    """在字典中查找"""
    if name in dict:
        print("作业1 {} 作业2 {} 期末考试 {} 总成绩 {}".format(dict[name][1],dict[name][2],dict[name][3],dict[name][4]))
    else:
        print("名字不存在！")

#主程序
import csv

file1 = open("newscore.csv","r",encoding = "UTF-8")

dict1={}
file_to_dict(file1,dict1)
name = input("请输入一个名字")
inqury(name,dict1)
