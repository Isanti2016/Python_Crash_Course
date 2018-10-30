# -*- coding:utf-8 -*-

import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	"""显示得分类"""

	def __init__(self, ai_settings, screen, stats):
		"""初始化显示得分类"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		#显示得分信息时使用的字体设置
		self.text_color = (30, 30, 30)
		self.font  = pygame.font.SysFont(None, 48)

		self.prep_score()
		self.prep_hight_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""将得分转换为图像"""
		#score_str = str(self.stats.score)
		#转化为整十的数字，并用“，”分隔开
		round_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(round_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

		#将得分放在指定位置
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_hight_score(self):
		"""将最高得分转换为图像"""
		#转化为整十的数字，并用“，”分隔开
		hight_round_score = int(round(self.stats.hight_score, -1))
		hight_score_str = "{:,}".format(hight_round_score)
		self.hight_score_image = self.font.render(hight_score_str, True, self.text_color, self.ai_settings.bg_color)

		#将得分放在指定位置
		self.hight_score_rect = self.hight_score_image.get_rect()
		self.hight_score_rect.centerx = self.screen_rect.centerx
		self.hight_score_rect.top = self.score_rect.top

	def prep_level(self):
		"""等级转换为图像"""
		self.level_image = self.font.render(str(self.stats.level)
							, True, self.text_color, self.ai_settings.bg_color)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""显示还剩飞船数量"""
		self.ships = Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)

	def show_score(self):
		"""在屏幕显示得分,最高分，等级，飞船数量"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.hight_score_image, self.hight_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)