# coding=utf-8

class Settings():
    """存储设置信息"""
    
    def __init__(self):
        """初始化设置"""
        
        self.screen_width = 950
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        #飞船速度控制       
        self.ship_limit = 3

        #子弹设置       
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 500

        #外星人设置      
        self.alien_speedy_factor = 50

        #加速度尺度
        self.speedup_scale = 2
        #外星人点数提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
    	"""初始化游戏设置"""
    	self.ship_speed_factor = 2.5
    	self.bullet_speed_factor = 2
    	self.alien_speedx_factor = 1
    	self.alien_fleet_direction = 1
    	#计算一个外星人的得分
    	self.alien_point = 50


    def increase_speed(self):
    	"""调高速度"""
    	self.ship_speed_factor *= self.speedup_scale
    	self.bullet_speed_factor *= self.speedup_scale
    	self.alien_speedx_factor *= self.speedup_scale
    	self.alien_point = int(self.alien_point * self.score_scale)



