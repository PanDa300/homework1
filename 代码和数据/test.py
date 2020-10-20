import re

file_in1 = open('seg&pos.txt', 'r')
file_in2 = open('seg_BMM.txt', 'r')
cnt = 0
f = file_in1.readlines()
num = 0
for line in file_in2.readlines():
    line1 = re.split('###', line)   # 正则表达式分块
    line2 = re.split('[/|\[|\]][a-zA-Z]*[ ]*', f[cnt])  # 正则表达式分块
    if line1 == line2:
        print(cnt)
        num += 1
    cnt += 1
print(num / cnt)  # 正确率为正确句子数/错误句子数
