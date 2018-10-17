"""
飞机大战游戏的全局配置信息
"""
import os
import tkinter as tk
import random as rd


"""
游戏的各配置项
"""
game_flag = ''

# 游戏窗口的标题及边界
window_title = "Plane Warface Game"
window_boundary_row = 600
window_boundary_col = 480

# 角色的生命状态
life_status_alive = 0   # 活动
life_status_dead = 1    # 死亡
life_status_reset = 2   # 重置

# 角色生命值
lives_num_enemy = 1
lives_num_hero = 3


# 游戏中部件图像所在路径及各部件图像文件名
images_path = os.getcwd()+ os.path.join("/Images/")
filename_suffix = ".gif"
filename_sky = "background"
filename_pause = "pause"
filename_start = "start"
filename_start_label = "start_label"
filename_gameover = "gameover"
filename_smallplane = "smallplane"
filename_bee = "bee"
filename_bigplane = "bigplane"
filename_bullet = "bullet"
filename_hero = "hero"
filename_default = filename_hero

# 游戏中各部件图像的宽与高
image_sky_width = 480
image_sky_height = 852
image_pause_width = 400
image_pause_height = 654
image_start_width = 400
image_start_height = 654
image_gameover_width = 400
image_gameover_height = 654
image_smallplane_width = 49
image_smallplane_height = 36
image_bigplane_width = 69
image_bigplane_height = 99
image_bullet_width = 8
image_bullet_height = 14
image_hero_width = 97
image_hero_height = 124
image_bee_width = 60
image_bee_height = 50

# 游戏中部件的初始锚点及对应初始显示位置坐标
# 天空 - 将图片的右下角显示在画布的(480,600)的坐标处
#       如下部件以相同方式进行显示
initial_anchor_sky_1 = tk.SE
initial_anchor_sky_x_1 = window_boundary_col
initial_anchor_sky_y_1 = window_boundary_row
# 暂停 - 窗口内部居中显示
initial_anchor_pause = tk.CENTER
initial_anchor_pause_x = window_boundary_col / 2
initial_anchor_pause_y = window_boundary_row / 2
# 开始 - 窗口内部居中显示
initial_anchor_start = tk.CENTER
initial_anchor_start_x = window_boundary_col / 2
initial_anchor_start_y = window_boundary_row / 2
# 结束 - 窗口内部居中显示
initial_anchor_gameover = tk.CENTER
initial_anchor_gameover_x = window_boundary_col / 2
initial_anchor_gameover_y = window_boundary_row / 2
# 敌军小飞机 - x轴上方开始向下移动，具体从x轴的哪个点开始是随机的
initial_anchor_smallplane = tk.SW
initial_anchor_smallplane_x = rd.randint(0, window_boundary_col-image_smallplane_width)
initial_anchor_smallplane_y = 0
# 敌军大飞机 - x轴上方开始向下移动，具体从x轴的哪个点开始是随机的
initial_anchor_bigplane = tk.SW
initial_anchor_bigplane_x = rd.randint(0, window_boundary_col - image_bigplane_width)
initial_anchor_bigplane_y = 0
# 敌军小蜜蜂 - x轴上方开始向下移动，具体从x轴的哪个点开始是随机的
initial_anchor_bee = tk.NW
initial_anchor_bee_x = rd.randint(0, window_boundary_col - image_bee_width)
initial_anchor_bee_y = 0
# 己方战机 - 出现在窗口的下三分之一处并水平居中
initial_anchor_hero = tk.CENTER
initial_anchor_hero_x = window_boundary_col / 2
initial_anchor_hero_y = window_boundary_row / 3 * 2
# 己方子弹 - 出现在己方战机的上方中间
initial_anchor_bullet = tk.CENTER
initial_anchor_bullet_x = window_boundary_col / 2
initial_anchor_bullet_y = window_boundary_row / 3 * 2

# 游戏中各部件的移动步长
step_length_default = 1
step_length_sky_x = 0
step_length_sky_y = 10
step_length_smallplane_x = 0
step_length_smallplane_y = 5
step_length_bigplane_x = 0
step_length_bigplane_y = 3
step_length_bee_x = 5
step_length_bee_y = 3
step_length_bullet_x = 0
step_length_bullet_y = 12
step_length_hero_x = 5
step_length_hero_y = 5

# 记录生成各种部件的计数
total_number_hero = 0
total_number_bullet = 0
total_number_smallplane = 0
total_number_bigplane = 0
total_number_bee = 0

# 记录当前各种部件的数目
current_bullet_num = 1
current_number_hero = 0
current_number_smallplane = 0
current_number_bigplane = 0
current_number_bee = 0


# 击落敌军的奖励分数
score_enemy_small = 2
score_enemy_big = 5
score_enemy_bee = 1
score_highest = 10


# 标识项
bullet_create_flag = 1
hero_move_flag = True
break_record_flag = False
hero_aircraft_death = False

# 击落战机数量
defeat_big_nums = 0
defeat_small_nums = 0
defeat_bee_nums = 0
