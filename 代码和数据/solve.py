import re


def not_empty(s):  # 判断是否为空
    return s and s.strip()


file_in1 = open('sent.txt', 'r')
file_in2 = open('dict.txt', 'r')
file_out = open('seg_BMM.txt', 'w')

dict_now = re.split('[ ]+', file_in2.readline())  # 正则表达式分块
dict_now = list(dict.fromkeys(dict_now).keys())  # 转变为dictionary去重
dict_now = list(filter(not_empty, dict_now))  # 除去空字符
dict_now.sort(key=lambda i: len(i), reverse=True)  # 对字符串进行排序
dictionary = []
for key in dict_now:
    dictionary.append(key.strip())  # 最后的词表
# print(dict_now)
# print(len(dict_now))
# print(len(file_in1.readlines()))

cnt = 0
for line in file_in1.readlines()[:1000]:
    cnt += 1
    # print(cnt)
    ans_now = []
    sam = line[19:len(line) - 1]
    # print(sam)
    lens = len(sam)
    # print(lens)
    while lens:
        maxn = min(lens, len(dictionary))
        word = sam[lens - maxn:lens]
        while word not in dictionary:
            if len(word) == 1:
                break
            word = word[1:]
        lens = lens - len(word)
        ans_now.insert(0, lens + 19)
    ans = list(line)
    # print(ans_now)
    for key in reversed(ans_now):
        ans.insert(key, '$$$')  # 将分词结果分隔
    # print(ans_now)
    file_out.write(''.join(ans))
    # print(''.join(ans))
    # break
file_in1.close()
file_in2.close()
file_out.close()
