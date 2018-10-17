# stderr.py


import sys

sys.stdout.write("我是标准输出\n")
sys.stderr.write("我是一个错误\n")


# 当用 
#   $ python3 stderr > mystdout.txt  2> err.txt
