import re 

# regex = re.compile(r'hello',re.I)

# l = regex.findall('hello Hello')
# print(l)

s = '''hello world
nihao Beijing'''

# l = re.findall(r'.+',s,re.S)
# print(l)

# obj = re.search(r"world$",s,re.M)
# print(obj.group())


pattern = r"""(?P<dog>\w+)  #dog组
\s+   #匹配任意多个空格
(\W+)  #匹配一些特殊字符
"""
#添加注释同时忽略大小写
s = re.match(pattern,'hello  %#@',re.X | re.I).group()
print(s)

