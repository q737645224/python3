import tkinter
import time
import random as rd
# import sys
# sys.path.append(".")
import config
import mover
import sky
import bigplane
import smallplane
import bee as honeybee
import hero as heroplane
import bullet


# 创建天空背景
def create_sky(root, canvas):
    sky_1 = sky.Sky(root, canvas,
                    config.initial_anchor_sky_1,
                    config.initial_anchor_sky_x_1,
                    config.initial_anchor_sky_y_1, "Sky01")

    sky_2 = sky.Sky(root, canvas, tkinter.SW, sky_1.nw[0], sky_1.nw[1], "Sky02")

    tmp_canvas_img = canvas.create_image(sky_1.anchor_x,
                                         sky_1.anchor_y,
                                         anchor=sky_1.anchor,
                                         image=sky_1.bg_image,
                                         tags=sky_1.bg_image_tags)
    sky_1.set_canvas_image(tmp_canvas_img)

    tmp_canvas_img = canvas.create_image(sky_2.anchor_x,
                                         sky_2.anchor_y,
                                         anchor=sky_2.anchor,
                                         image=sky_2.bg_image,
                                         tags=sky_2.bg_image_tags)
    sky_2.set_canvas_image(tmp_canvas_img)
    return [sky_1, sky_2]


# 移动天空，模拟前行
def move_sky(canvas, sky_1, sky_2):
    # 若sky_1已消失在窗口范围后，从重新移动到sky_2的上方
    if sky_1.nw[1] >= config.window_boundary_row - sky_1.steps[1]:
        canvas.move(sky_1.bg_image_tags, 0, -(config.image_sky_height+sky_1.nw[1]))
        sky_1.update_positions(0, -(config.image_sky_height+sky_1.nw[1]))
    # 若sky_2已消失在窗口范围后，从重新移动到sky_1的上方
    elif sky_2.nw[1] >= config.window_boundary_row - sky_2.steps[1]:
        canvas.move(sky_2.bg_image_tags, 0, -(config.image_sky_height+sky_2.nw[1]))
        sky_2.update_positions(0, -(config.image_sky_height+sky_2.nw[1]))
    # 正常移动
    else:
        sky_1.exec_move()
        sky_2.exec_move()


# 创建大飞机
def create_big_plane(root, canvas, enemy_list):
    # 大飞机
    x = rd.randint(0, config.window_boundary_col - config.image_bigplane_width)
    big_plane = bigplane.BigPlane(root, canvas, tkinter.SW, x, 0,"BigPlane")
    tmp_canvas_img = canvas.create_image(big_plane.anchor_x,
                                         big_plane.anchor_y,
                                         anchor=big_plane.anchor,
                                         image=big_plane.bg_image,
                                         tags=big_plane.bg_image_tags)
    big_plane.set_canvas_image(tmp_canvas_img)
    enemy_list.insert(0, big_plane)
    config.defeat_big_nums += 1


# 创建小飞机
def create_small_plane(root, canvas, enemy_list):
    # 小飞机
    x = rd.randint(0, config.window_boundary_col - config.image_smallplane_width)
    small_plane = smallplane.SmallPlane(root, canvas, tkinter.SW, x, 0, "SmallPlane")
    tmp_canvas_img = canvas.create_image(small_plane.anchor_x,
                                         small_plane.anchor_y,
                                         anchor=small_plane.anchor,
                                         image=small_plane.bg_image,
                                         tags=small_plane.bg_image_tags)
    small_plane.set_canvas_image(tmp_canvas_img)
    enemy_list.insert(0, small_plane)
    config.defeat_small_nums += 1


# 创建小蜜蜂
def create_bee(root, canvas, enemy_list):
    # 蜜蜂
    x = rd.randint(0, config.window_boundary_col - config.image_bee_width)
    bee = honeybee.Bee(root, canvas, tkinter.SW, x, 0, "Bee")
    tmp_canvas_img = canvas.create_image(bee.anchor_x,
                                         bee.anchor_y,
                                         anchor=bee.anchor,
                                         image=bee.bg_image,
                                         tags=bee.bg_image_tags)
    bee.set_canvas_image(tmp_canvas_img)
    enemy_list.insert(0, bee)
    config.defeat_bee_nums += 1


# 创建英雄机
def create_hero(root, canvas, lives):
    hero = heroplane.HeroPlane(root, canvas,
                       config.initial_anchor_hero,
                       config.initial_anchor_hero_x,
                       config.initial_anchor_hero_y,
                       "HeroPlane01", lives)
    tmp_canvas_img = canvas.create_image(hero.anchor_x,
                                         hero.anchor_y,
                                         anchor=hero.anchor,
                                         image=hero.bg_image,
                                         tags=hero.bg_image_tags)
    hero.set_canvas_image(tmp_canvas_img)
    return hero


# 创建英雄机
def create_bullet_tags(root, canvas, anchor, x, y, tags):
    blt = bullet.Bullet(root, canvas, anchor, x, y, tags)
    tmp_canvas_img = canvas.create_image(blt.anchor_x,
                                         blt.anchor_y,
                                         anchor=blt.anchor,
                                         image=blt.bg_image,
                                         tags=blt.bg_image_tags)
    blt.set_canvas_image(tmp_canvas_img)
    return blt


# 创建子弹
def create_bullet(root, canvas, mother, tag_id):
    # 每帧子弹
    blt_1 = create_bullet_tags(root, canvas,
                               tkinter.CENTER,
                               mother.nw[0]+mother.width/2,
                               mother.nw[1],
                               "BulletMid"+str(tag_id))
    return blt_1


# 创建敌机
def create_enemys(root, canvas):
    # 敌机列表中插入新敌机
    enemy_list = []
    create_big_plane(root, canvas, enemy_list)
    create_small_plane(root, canvas, enemy_list)
    create_bee(root, canvas, enemy_list)
    return enemy_list


# 移动敌机
def move_enemy(root, canvas, enemy):
    enemy_list = enemy
    global ENEMY_DEAD_INDEX

    for item in enemy_list:
        if item.state is config.life_status_alive:
            item.exec_move()
        else:
            item.errors_happened()
        # else:
        #     dead_image = item.get_dead_images()[ENEMY_DEAD_INDEX]
        #     print("ENEMY_DEAD_INDEX: ", ENEMY_DEAD_INDEX)
        #     canvas.create_image(item.nw[0], item.nw[1],
        #                         anchor=tkinter.NW,
        #                         image=dead_image,
        #                         tags="PlayDeath")
        #     root.update()
        #     ENEMY_DEAD_INDEX += 1


# 创建己方战机
def create_owns(root, canvas):
    hero = create_hero(root, canvas, config.lives_num_hero)
    bullet = create_bullet(root, canvas, hero, config.current_bullet_num)
    config.current_bullet_num += 1
    return [hero, bullet]


# 移动己方战机
def move_owns(root, canvas, own_list):
    for item in own_list:
        if item.state is config.life_status_alive:
            item.exec_move()
        else:
            item.errors_happened()


# 碰撞测试
def check_collision(root, canvas, enemy, own):
    # 英雄机与敌机的碰撞
    for item in enemy:
        if own[0].is_hit_another(item):
            own[0].update_life_status()
            own[0].errors_happened()

            item.update_life_status()
            item.errors_happened()
            enemy.remove(item)

            # 创建新敌机
            item_type = item.bg_image_tags
            if item_type is "Bee":
                create_bee(root, canvas, enemy)
            elif item_type is "SmallPlane":
                create_small_plane(root, canvas, enemy)
            elif item_type is "BigPlane":
                create_big_plane(root, canvas, enemy)
            else:
                print("enemy hits error")

            # 删除画布中己方战机并新建
            lives = own[0].lives_num
            if lives == 0:
                config.hero_aircraft_death = True
            for i in own:
                canvas.delete(i.bg_image_tags)
            new_hero = create_hero(root, canvas, lives)
            new_bullet = create_bullet(root, canvas, new_hero, config.current_bullet_num)
            own.clear()
            own.append(new_hero)
            own.append(new_bullet)


            return enemy, own

    # 子弹击中敌机
    for item in enemy:
        for blt in own[1:]:
            if item.is_hit_another(blt):
                # 播放死亡动画
                blt.update_life_status()
                blt.errors_happened()
                own.remove(blt)

                item.update_life_status()
                item.errors_happened()
                enemy.remove(item)

                # 创建新敌机
                item_type = item.bg_image_tags
                if item_type is "Bee":
                    create_bee(root, canvas, enemy)
                elif item_type is "SmallPlane":
                    create_small_plane(root, canvas, enemy)
                elif item_type is "BigPlane":
                    create_big_plane(root, canvas, enemy)
                else:
                    print("enemy hits error")

                return enemy, own

    return enemy, own


# 创建图片
def create_img(filename):
    start_image_fullname = config.images_path + filename + config.filename_suffix
    return tkinter.PhotoImage(file=start_image_fullname)


# 删除画布上图片
def delete_canvas_img(canvas, tags):
    print('delete_canvas_img')
    canvas.delete(tags)


# 开始游戏
def start_game(event, root, canvas):
    print('start_game')

    # 游戏标志
    config.game_flag = 'start'

    # 屏蔽开始界面
    # delete_canvas_img(canvas, "Start")
    canvas.move("Start", 0, config.window_boundary_row*3/2)

    # 创建天空
    sky_first, sky_second = create_sky(root, canvas)

    # 创建敌方战机
    enemy_list = create_enemys(root, canvas)

    # 创建己方战机
    own_list = create_owns(root, canvas)

    root.update()

    # 定时更新数据
    while config.game_flag == 'start':
        # 移动天空、
        # 敌机、己机
        move_sky(canvas, sky_first, sky_second)
        move_enemy(root, canvas, enemy_list)
        move_owns(root, canvas, own_list)

        # 每帧创建一个新子弹
        new_blt = create_bullet(root, canvas, own_list[0], config.current_bullet_num)
        config.current_bullet_num += 1
        own_list.append(new_blt)

        # 碰撞测试
        enemy_list, own_list = \
            check_collision(root, canvas, enemy_list, own_list)

        # 更新窗口画面
        root.update()

        # 打印得分
        # 打印当前成绩
        mygrade = config.defeat_big_nums * config.score_enemy_big \
                  + config.defeat_small_nums * config.score_enemy_small \
                  + config.defeat_bee_nums * config.score_enemy_bee
        if mygrade > config.score_highest:
            config.break_record_flag = True
            config.score_highest = mygrade
        # print("my_grade:　", mygrade)

        canvas.delete("Grade")
        canvas.create_text((5, 5),
                           fill='red',
                           font=('Helvetica', 20, 'bold'),
                           text="得分:"+str(mygrade),
                           anchor=tkinter.NW,
                           tag="Grade")
        # 打印最高记录
        canvas.delete("Highest")
        canvas.create_text((config.window_boundary_col/2, 5),
                           fill='blue',
                           font=('Helvetica', 20, 'bold'),
                           text="最高分:" + str(config.score_highest),
                           anchor=tkinter.N,
                           tag="Highest")
        # 打印生命值
        canvas.delete("Lives")
        canvas.create_text((config.window_boundary_col-10, 5),
                           fill='#000fff000',
                           font=('Helvetica', 20, 'bold'),
                           text="生命:" + str(own_list[0].lives_num),
                           anchor=tkinter.NE,
                           tag="Lives")

        root.update()
        if config.hero_aircraft_death:
            quit_game('',root,canvas)

        time.sleep(0.0333)


# 暂停游戏
def pause_game(event, root, canvas):
    print('pause_game')
    # 创建暂停界面
    config.game_flag = 'pause'
    canvas.move("Pause", 0, config.window_boundary_row)


# 退出游戏
def quit_game(event, root, canvas):
    print('quit_game')
    config.game_flag = 'quit'
    canvas.delete("all")
    if config.break_record_flag:
        canvas.create_text((config.window_boundary_col/2, config.window_boundary_row/2-50),
                           fill='#000fff000',
                           font=('Fixdsys', 36, 'bold'),
                           text="恭喜您！\n最高成绩:"+str(config.score_highest)+"\n打破历史纪录！",
                           anchor=tkinter.CENTER)
    else:
        canvas.create_text((config.window_boundary_col / 2, config.window_boundary_row / 2),
                           fill='#fff000000',
                           font=('Fixdsys', 36, 'bold'),
                           text="挑战失败！\n继续加油哦！",
                           anchor=tkinter.CENTER)

    root.update()
    time.sleep(3)
    quit()


# 程序入口函数
def main():
    # 创建游戏窗口
    root_window = tkinter.Tk()
    root_window.title("PlaneWarfareGame")
    root_window.resizable(width=False, height=False)

    # 创建画布
    window_canvas = tkinter.Canvas(root_window,
                                   width=config.window_boundary_col,
                                   height=config.window_boundary_row)
    window_canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)

    # 创建开始界面
    start_img = create_img(config.filename_start)
    window_canvas.create_image(config.window_boundary_col / 2,
                               config.window_boundary_row / 2,
                               anchor=tkinter.CENTER,
                               image=start_img,
                               tags="Start")
    # 创建暂停界面
    pause_img = create_img(config.filename_pause)
    window_canvas.create_image(config.window_boundary_col / 2,
                               -(config.window_boundary_row / 2),
                               anchor=tkinter.CENTER,
                               image=pause_img,
                               tags="Pause")

    # 点击界面开始游戏
    root_window.bind('<KeyPress-space>', lambda event: start_game(event, root_window, window_canvas))
    root_window.bind('<KeyPress-q>', lambda event: quit_game(event, root_window, window_canvas))
    root_window.bind('<KeyPress-Escape>', lambda event: quit_game(event, root_window, window_canvas))

    tkinter.mainloop()

# ========================================================================= #

main()
