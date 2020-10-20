import re


def not_empty(s):  # 判断是否为空
    return s and s.strip()


file_in = open('seg&pos.txt', 'r')
file_out = open('dict.txt', 'w')

ans = ['']
for line in file_in.readlines()[:1000]:
    line_now = re.split('[/|\[|\]][a-zA-Z]*[ ]*', line)  # 正则表达式分块
    ans.extend(line_now[1:])
ans = list(dict.fromkeys(ans).keys())  # 转变为dictionary去重
ans = list(filter(not_empty, ans))  # 除去空字符
ans.sort(key=lambda i: len(i), reverse=True)  # 对字符串进行排序
for line in ans:
    file_out.write(line + ' ')
file_in.close()
file_out.close()
