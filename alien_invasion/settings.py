class Settings():
    '''存储所有设置的类'''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 8

        # 子弹设置
        self.bullet_speed_factor = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3