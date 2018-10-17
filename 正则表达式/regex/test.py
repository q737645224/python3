import re 

f = open("test.txt")

l = []

#大写字母开头单词
# pattern = r'\b[A-Z][\._0-9a-zA-Z]*'

#数字
pattern = r'-?\d+\.?/?\d*%?'


for line in f:
    l += re.findall(pattern,line)
print(l)


