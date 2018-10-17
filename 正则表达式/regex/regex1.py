import re 

# obj = re.finditer(r"\d+",'2008年事情有点多,512地震,08奥运')

#迭代出的内容是match对象
# for i in obj:
    # print(dir(i))
    # print(i.group())

# try:
#     obj = re.fullmatch(r'\w+','abc123')
#     print(obj.group())
# except AttributeError as e:
#     print(e)

# obj = re.match(r'foo','foo,food on the table')
# print(obj.group())

obj = re.search(r'foo','Foo,food on the table,foo')
print(obj.group())