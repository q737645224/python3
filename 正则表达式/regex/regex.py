import re 

pattern = r"([A-Z])(\S+)"

#re调用
# l = re.findall(pattern,'Hello World')
# print(l)

#compile对象调用
# regex = re.compile(pattern)
# l = regex.findall("Hello World",3,20)
# print(l)

# l = re.split(r'\W','hi#asaf@对方%asdf')
# print(l)

# s = re.sub(r'\s+','##',"This is a boy")
s = re.subn(r'\s+','##',"This is a boy")
print(s)