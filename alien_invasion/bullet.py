# -*- coding: utf-8 -*-
# @Author: wangbei
# @Date:   2018-10-16 00:41:56
# @Last Modified by:   wangbei
# @Last Modified time: 2018-10-18 00:40:10

import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	"""docstring for Bullet"""
	def __init__(self, ai_settings, screen, ship):
		super(Bullet, self).__init__()
		self.screen = screen

		#创建子弹，设置正确的位置
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		#小数值存储子弹的位置，更精确的控制
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	#相当于对精灵Goup中update重定义
	def update(self):
		"""子弹更新位置"""
		self.y -= self.speed_factor
		#把小数再次转换为整数
		self.rect.y = self.y

	def draw_bullet(self):
		"""屏幕绘制子弹"""
		pygame.draw.rect(self.screen, self.color, self.rect)