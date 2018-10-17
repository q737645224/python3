import tkinter
import time
import config


class BaseMover(object):
    """所有移动者的基本类"""

    def __init__(self, root, canvas, position, x, y, tags, w, h, play):
        # 窗口及画布
        self.root = root
        self.canvas = canvas
        # 移动者的状态
        self.state = config.life_status_alive
        # 移动者加载背景图像的锚点及对应坐标
        # 默认图片加载到左上角
        self.anchor = position
        self.anchor_x = x
        self.anchor_y = y
        # 尺寸
        self.width = w
        self.height = h
        # 加载图片的标签
        self.bg_image_tags = tags
        # 击落移动者播放的死亡图像
        self.do_dead_play = play
        self.dead_image_index = [0, 1, 2, 3, 4]
        # 当前图片四个角的坐标
        self.nw = self.get_anchor_nw_position()
        self.ne = self.get_anchor_ne_position()
        self.sw = self.get_anchor_sw_position()
        self.se = self.get_anchor_se_position()
        self.center = self.get_anchor_center_position()
        # 画布上图像下标
        self.canvas_img_index = 0
        # 对象当前生命值
        self.lives_num = 1

    # 获取左上角坐标值
    def get_anchor_nw_position(self):
        if self.anchor == tkinter.NW:
            return [self.anchor_x, self.anchor_y]
        elif self.anchor == tkinter.NE:
            return [self.anchor_x-self.width, self.anchor_y]
        elif self.anchor == tkinter.SW:
            return [self.anchor_x, self.anchor_y-self.height]
        elif self.anchor == tkinter.SE:
            return [self.anchor_x-self.width, self.anchor_y-self.height]
        elif self.anchor == tkinter.CENTER:
            return [self.anchor_x - self.width/2, self.anchor_y - self.height/2]
        else:
            return [0, 0]

    # 获取右上角坐标值
    def get_anchor_ne_position(self):
        if self.anchor == tkinter.NW:
            return [self.anchor_x+self.width, self.anchor_y]
        elif self.anchor == tkinter.NE:
            return [self.anchor_x, self.anchor_y]
        elif self.anchor == tkinter.SW:
            return [self.anchor_x+self.width, self.anchor_y-self.height]
        elif self.anchor == tkinter.SE:
            return [self.anchor_x, self.anchor_y-self.height]
        elif self.anchor == tkinter.CENTER:
            return [self.anchor_x+self.width/2, self.anchor_y-self.height/2]
        else:
            return [self.width, 0]

    # 获取左下角坐标值
    def get_anchor_sw_position(self):
        if self.anchor == tkinter.NW:
            return [self.anchor_x, self.anchor_y+self.height]
        elif self.anchor == tkinter.NE:
            return [self.anchor_x-self.width, self.anchor_y]
        elif self.anchor == tkinter.SW:
            return [self.anchor_x, self.anchor_y]
        elif self.anchor == tkinter.SE:
            return [self.anchor_x-self.width, self.anchor_y]
        elif self.anchor == tkinter.CENTER:
            return [self.anchor_x-self.width/2, self.anchor_y+self.height/2]
        else:
            return [0, self.height]

    # 获取右下角坐标值
    def get_anchor_se_position(self):
        if self.anchor == tkinter.NW:
            return [self.anchor_x - self.width, self.anchor_y - self.height]
        elif self.anchor == tkinter.NE:
            return [self.anchor_x, self.anchor_y + self.height]
        elif self.anchor == tkinter.SW:
            return [self.anchor_x + self.width, self.anchor_y]
        elif self.anchor == tkinter.SE:
            return [self.anchor_x, self.anchor_y]
        elif self.anchor == tkinter.CENTER:
            return [self.anchor_x+self.width/2, self.anchor_y+self.height/2]
        else:
            return [self.width, self.height]

    # 获取中心坐标值
    def get_anchor_center_position(self):
        if self.anchor == tkinter.NW:
            return [self.anchor_x + self.width/2, self.anchor_y + self.height/2]
        elif self.anchor == tkinter.NE:
            return [self.anchor_x - self.width/2, self.anchor_y + self.height/2]
        elif self.anchor == tkinter.SW:
            return [self.anchor_x + self.width/2, self.anchor_y - self.height/2]
        elif self.anchor == tkinter.SE:
            return [self.anchor_x - self.width/2, self.anchor_y - self.height/2]
        elif self.anchor == tkinter.CENTER:
            return [self.anchor_x, self.anchor_y]
        else:
            return [self.width/2, self.height/2]

    # 设置画布上图片
    def set_canvas_image(self, cimg):
        self.canvas_img_index = cimg

    # 获取画布上图片
    def get_canvas_image(self):
        return self.canvas_img_index

    # 删除画布上图片
    def del_canvas_image(self, tags):
        self.canvas.delete(tags)

    # 指定对象的移动
    def base_move(self, tags, x, y):
        self.canvas.move(tags, x, y)
        self.update_positions(x, y)

    # 更新坐标值
    def update_positions(self, x, y):
        for i in [self.nw, self.ne, self.se, self.sw, self.center]:
            i[0] += x
            i[1] += y

    # 设置当前生命值
    def set_lives_num(self, num):
        self.lives_num = num

    # 更改生命状态
    def update_life_status(self):
        self.lives_num -= 1
        if self.lives_num <= 0:
            self.state = config.life_status_dead
        else:
            self.state = config.life_status_reset

    # 是否发生碰撞
    def is_hit_another(self, another_mover):
        # print(self, 'self.NW_x = %f, self.NW_y = %f' % (self.nw[0], self.nw[1]))
        # print(another_mover, 'another_mover.SE_x = %f, another_mover.SE_y = %f'
        #       % (another_mover.se[0], another_mover.se[1]))

        # another的左上角 - 是否撞击上当前对象
        bool_nw_x = self.nw[0] < another_mover.nw[0] < self.ne[0]
        bool_nw_y = self.nw[1] < another_mover.nw[1] < self.sw[1]

        # another的右上角 - 是否撞击上当前对象
        bool_ne_x = self.nw[0] < another_mover.ne[0] < self.ne[0]
        bool_ne_y = self.nw[1] < another_mover.ne[1] < self.sw[1]

        # another的左下角 - 是否撞击上当前对象
        bool_sw_x = self.nw[0] < another_mover.sw[0] < self.ne[0]
        bool_sw_y = self.nw[1] < another_mover.sw[1] < self.sw[1]

        # another的右下角 - 是否撞击上当前对象
        bool_se_x = self.nw[0] < another_mover.se[0] < self.ne[0]
        bool_se_y = self.nw[1] < another_mover.se[1] < self.sw[1]

        if (bool_nw_x and bool_nw_y) \
                or (bool_ne_x and bool_ne_y) \
                or (bool_sw_x and bool_sw_y) \
                or (bool_se_x and bool_se_y):
            # print(type(self), type(another_mover))
            # print(bool_nw_x, bool_nw_y, bool_ne_x, bool_ne_y, bool_sw_x, bool_sw_y, bool_se_x, bool_se_y)
            return True
        else:
            return False

    # 错误发生后或重置或死亡
    def errors_happened(self):
        if self.state is config.life_status_dead:
            self.del_canvas_image(self.bg_image_tags)
        elif self.state is config.life_status_reset:
            x = 0
            y = 0
            if self.anchor == tkinter.NW:
                x = self.anchor_x - self.nw[0]
                y = self.anchor_y - self.nw[1]
            elif self.anchor == tkinter.NE:
                x = self.anchor_x - self.ne[0]
                y = self.anchor_y - self.ne[1]
            elif self.anchor == tkinter.SW:
                x = self.anchor_x - self.sw[0]
                y = self.anchor_y - self.sw[1]
            elif self.anchor == tkinter.SE:
                x = self.anchor_x - self.se[0]
                y = self.anchor_y - self.se[1]
            elif self.anchor == tkinter.CENTER:
                x = self.anchor_x - self.center[0]
                y = self.anchor_y - self.center[1]

            self.canvas.move(self.bg_image_tags, x, y)
            self.state = config.life_status_alive

