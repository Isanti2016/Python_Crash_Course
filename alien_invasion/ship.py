# -*- coding: utf-8 -*-
# @Author: wangbei
# @Date:   2018-10-14 22:19:01
# @Last Modified by:   wangbei
# @Last Modified time: 2018-10-29 00:19:00

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

	def __init__(self, ai_setting, screen):
		"""初始化飞船"""
		super(Ship, self).__init__()
		#获取要绘制飞船的屏幕
		self.screen = screen
		self.ship_speed_factor = ai_setting

		# 加载飞船图像,获得飞船外形
		self.image = pygame.image.load("images/ship.bmp")
		self.rect  = self.image.get_rect()

		self.screen_rect = screen.get_rect()

		#设置飞船的位置
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom  = self.screen_rect.bottom

		#移动标志
		self.moving_right = False
		self.moving_left = False
		#存储飞船速度小数值
		self.center = float(self.rect.centerx)

	def blitme(self):
		"""在指定的屏幕和位置绘制飞船"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""根据标志进行移动"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ship_speed_factor

		self.rect.centerx = self.center

	def center_ship(self):
		self.center = self.screen_rect.centerx