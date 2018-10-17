# 练习:
#   写一个类Bicycle类 ,有 run方法.调用时显示骑行里程km
#     class Bicycle:
#         def run(self, km):
#             print('自行车骑行了', km, '公里')
#   再写一个类EBicycle(电动自行车类), 在Bicycle类的基础上添加了电池电量 volume 属性, 有两个方法:
#      1. fill_charge(self, vol)  用来充电, vol为电量
#      2. run(self, km) 方法每骑行10km消耗电量1度,同时显示当前电量,当电量耗尽时调用 父类的run方法继续骑行

#     b = EBicycle(5)  # 新买的电动有内有5度电
#     b.run(10)  # 电动骑行了10km还剩 4 度电
#     b.run(100)  #电动骑行了40km,还剩0度电,其余60用脚登骑行
#     b.fill_charge(10)  # 又充了10度电
#     b.run(50)  # 骑行了50公里剩5度电


class Bicycle:
    def run(self, km):
        print('自行车骑行了', km, '公里')


# 1. fill_charge(self, vol)  用来充电, vol为电量
# 2. run(self, km) 方法每骑行10km消耗电量1度,同时显示当前电量,当电量耗尽时调用 父类的run方法继续骑行
class EBicycle(Bicycle):
    def __init__(self, vol):
        self.volume = vol  # 电量

    def fill_charge(self, vol):
        self.volume += vol
        print("电动自行车充电%d度" % vol)

    def run(self, km):
        # 先算电走的里程,和要行驶的里程,哪儿个最小
        e_km = min(km, self.volume * 10)  # 电行驶里程
        self.volume -= e_km / 10  # 消耗电量
        if e_km > 0:
            print("电动自行车骑行了", e_km, '公里,剩余电量',
                  self.volume, '度')
        if km > e_km:  # 有路程没走完
            super().run(km - e_km)

b = EBicycle(5)  # 新买的电动有内有5度电
b.run(10)  # 电动骑行了10km还剩 4 度电
b.run(100)  #电动骑行了40km,还剩0度电,其余60用脚登骑行
b.fill_charge(10)  # 又充了10度电
b.run(50)  # 骑行了50公里剩5度电



