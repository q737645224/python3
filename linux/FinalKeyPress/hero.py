import tkinter
import mover
import config


class HeroPlane(mover.BaseMover):
    '''
        移动的敌机 - 大飞机
    '''
    def __init__(self, root, canvas, position, x, y, tags, lives):
        super().__init__(root, canvas, position, x, y, tags,
                         config.image_hero_width, config.image_hero_height, True)

        # 移动者的移动步长
        self.steps = [config.step_length_hero_x, config.step_length_hero_y]
        # 移动方向 - 向上
        self.move_direction = [0, -1]
        # 移动者加载背景图像
        self.bg_image_fullname = config.images_path + config.filename_hero + config.filename_suffix
        self.bg_image = tkinter.PhotoImage(file=self.bg_image_fullname)
        # 重置生命值
        super().set_lives_num(lives)
        # root.bind('<B1-Motion>', self.follow_mouse)
        root.bind('<KeyPress-Left>', self.key_press)
        root.bind('<KeyPress-Right>', self.key_press)
        root.bind('<KeyPress-Up>', self.key_press)
        root.bind('<KeyPress-Down>', self.key_press)
        # root.bind('<ButtonRelease-1>', self.Release_mouse)

    def exec_move(self):
        if 0 < self.nw[0] and 0 < self.nw[1] \
                and self.se[0] < config.window_boundary_col \
                and self.se[1] < config.window_boundary_row:
            # X/Y轴边界之内正常移动
            x = self.steps[0] * self.move_direction[0]
            y = self.steps[1] * self.move_direction[1]
            # print(self, x, y)
            self.base_move(self.bg_image_tags, x, y)
        else:
            # 不执行跨越边界的操作
            if self.nw[0] <= 0:
                self.base_move(self.bg_image_tags, 1, 0)
            if self.nw[1] <= 0:
                self.base_move(self.bg_image_tags, 0, 1)
            if self.se[0] >= config.window_boundary_col:
                self.base_move(self.bg_image_tags, -1, 0)
            if self.se[1] >= config.window_boundary_row:
                self.base_move(self.bg_image_tags, 0, -1)

    # 获取死亡图片
    def get_dead_images(self):
        img = []
        if self.do_dead_play:
            for i in self.dead_image_index:
                image_fullname = config.images_path + config.filename_hero + str(i) + config.filename_suffix
                image = tkinter.PhotoImage(file=self.bg_image_fullname)
                img.append(image)
            return img

    # 己方英雄跟随按键移动
    def key_press(self, event):
        code = event.keysym
        #print(event, "current_key_code: ", code)

        if code == "Up":  # 上
            self.move_direction = [0, -1]
        elif code == "Down":  # 下
            self.move_direction = [0, 1]
        elif code == "Left":  # 左
            self.move_direction = [-1, 0]
        elif code == "Right":  # 右
            self.move_direction = [1, 0]

    # 己方英雄跟随鼠标移动
    def follow_mouse(self, event):
        mouse = [event.x, event.y]
        item = self
        # print(event, "current_mouse_pos: ", mouse)
        # Y轴移动方向
        if mouse[1] > item.center[1]:
            item.move_direction[1] = 1
        elif mouse[1] < item.center[1]:
            item.move_direction[1] = -1
        else:
            item.move_direction[1] = 0

        # X轴移动方向
        if mouse[0] > item.center[0]:
            item.move_direction[0] = 1
        elif mouse[0] < item.center[0]:
            item.move_direction[0] = -1
        else:
            item.move_direction[0] = 0

        # print("item.move_direction ->", item.move_direction)


    def Release_mouse(self, event):
        print("into  Release_mouse: ",event)

