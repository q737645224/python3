import tkinter
import mover
import config


class Bullet(mover.BaseMover):
    '''
        移动的乙方子弹
    '''
    def __init__(self, root, canvas, position, x, y, tags):
        super().__init__(root, canvas, position, x, y, tags,
                         config.image_bullet_width, config.image_bullet_height, False)

        # 移动者的移动步长
        self.steps = [config.step_length_bullet_x, config.step_length_bullet_y]
        # 移动方向 - 向上
        self.move_direction = [0, -1]
        # 移动者加载背景图像
        self.bg_image_fullname = config.images_path + config.filename_bullet + config.filename_suffix
        self.bg_image = tkinter.PhotoImage(file=self.bg_image_fullname)
        # # 重置生命值
        # super().set_lives_num(config.lives_num_enemy)

    def exec_move(self):
        if self.nw[1] < config.window_boundary_row:
            # Y轴边界之内正常移动
            x = self.steps[0] * self.move_direction[0]
            y = self.steps[1] * self.move_direction[1]
            self.base_move(self.bg_image_tags, x, y)
        else:
            # Y轴边界之外错误处理
            self.update_life_status()
            self.errors_happened()

    # 获取死亡图片
    def get_dead_images(self):
        img = []
        if self.do_dead_play:
            for i in self.dead_image_index:
                image_fullname = config.images_path + config.filename_bullet + str(i) + config.filename_suffix
                image = tkinter.PhotoImage(file=self.bg_image_fullname)
                img.append(image)
            return img

