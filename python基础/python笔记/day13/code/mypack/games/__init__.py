
# mypack/games/__init__.py

# 此列表的作用是在from mypack.games import *时只导入:
# contra 和 tanks 模块

__all__ = ['contra', 'tanks']

print("games子包被加载")

