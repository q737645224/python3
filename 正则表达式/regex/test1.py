import re 
import sys 

def getAddress(port):
    f = open('1.txt')
    while True:
        data = ''
        #获取每一段内容
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        #文件结尾跳出循环
        if not data:
            break
        #匹配到每段的首个单词
        PORT = re.match(r'\S+',data).group()
        #判断是否为目标段
        if PORT == port:
            pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
            addr = re.search(pattern,data).group(1)
            return addr

if __name__ == "__main__":
    port = sys.argv[1]
    print(getAddress(port))