import csv

original_file = open("score.csv","r",encoding='UTF-8')

reader = csv.reader(original_file)

read_list = []
for row in reader:
    read_list.append(row)

original_file.close()

#计算行的平均值
average_row = 0
for i in range(1,4):
    cont_row = 0
    for j in range(1,4):
        cont_row+= int(read_list[i][j])
    average_row = cont_row/3
    read_list[i][4] = cont_row
    read_list[i][5] = average_row

#计算列的平均值
average_column = 0
for i in range(1,6):
    cont_column = 0
    for j in range(1,4):
        cont_column += int(read_list[j][i])
    average_column =cont_column/3
    read_list[4][i] = average_column


new_file = open("newscore.csv","w",newline = '',encoding = 'UTF-8')

writer = csv.writer(new_file)

for row in read_list:
    writer.writerow(row)
new_file.close()

