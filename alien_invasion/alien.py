# -*- coding: utf-8 -*-


import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	
	def __init__(self, ai_settings, screen):
		"""初始化外星人"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#加载外星人
		self.image = pygame.image.load("images/alien.bmp")
		self.rect = self.image.get_rect()

		#外星人位置初始化
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#存储外星人准确的位置
		self.x = float(self.rect.x)

	def blitme(self):
		"""制定位置绘制外星人"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""控制移动外星人左右移动"""
		self.x += (self.ai_settings.alien_speedx_factor *
				 self.ai_settings.alien_fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		"""检查外星人是否位于边缘"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		if self.rect.left <= 0:
			return True




