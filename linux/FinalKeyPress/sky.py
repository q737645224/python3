import tkinter
import mover
import config


class Sky(mover.BaseMover):
    '''
        移动的天空背景
    '''
    def __init__(self, root, canvas, position, x, y, tags):
        super().__init__(root, canvas, position, x, y, tags,
                         config.image_sky_width, config.image_sky_height, False)

        # 移动者的移动步长
        self.steps = [config.step_length_sky_x, config.step_length_sky_y]
        # 移动方向 - 向下
        self.move_direction = [0, 1]
        # 移动者加载背景图像
        self.bg_image_fullname = config.images_path + config.filename_sky + config.filename_suffix
        self.bg_image = tkinter.PhotoImage(file=self.bg_image_fullname)
        self.bg_image_tags = tags

    def exec_move(self):
        x = self.steps[0]*self.move_direction[0]
        y = self.steps[1] * self.move_direction[1]
        self.base_move(self.bg_image_tags, x, y)
