file1 = open("222.txt","r")

file1.readline()#使指针移到第二行

#The definiton of a word is must include more than three letters and less than 7 letters 

line_number = 2
for line_str in file1:
    cont = 0
    line_word_list = line_str.split()
    for word in line_word_list:
        if 3<=len(word)<=7:
            cont+=1
    print(line_number,line_str+'总共包含的单词数为',cont)
    line_number += 1
