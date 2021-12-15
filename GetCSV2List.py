
fo = open("price2016.csv", "r")
ls = []
for line in fo:
    print("replace之前：", line)
    line = line.replace("\n","")
    print('**********************************')
    print("replace之后：", line)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$S')
    ls.append(line.split(","))
print(ls)
fo.close()
