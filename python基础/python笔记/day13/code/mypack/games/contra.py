
# mypack/games/contra.py

def play():
    print("正在玩魂斗罗...")


def game_over():
    print("魂斗罗游戏结束")
    # 显示菜单 需要调用mypack/menu.py 里的show_menu
    # from mypack.menu import show_menu  # 绝对导入
    from ..menu import show_menu  # 相对导入
    # from ...mypack.menu import show_menu  # 错误
    show_menu()

print("魂斗罗模块被加载")



