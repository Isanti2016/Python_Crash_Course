# -*- coding: utf-8 -*-
import sys
import pygame
import time
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			ship.moving_left = True
		elif event.key == pygame.K_SPACE:
			fire_bullet(ai_settings, screen, ship, bullets)
		elif event.key == pygame.K_q:
			sys.exit()	

def check_keyup_events(event, ship):
	"""响应松开"""
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			ship.moving_left = False
def check_play_button(ai_settings, screen, ship, aliens, bullets,  event, stats, play_button, sb):
	if event.type == pygame.MOUSEBUTTONDOWN:
		(mouse_x, mouse_y) = pygame.mouse.get_pos()
		button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
		if button_clicked and not stats.game_active:
			stats.reset_stats()
			stats.game_active = True

			aliens.empty()
			bullets.empty()
			#重置游戏速度设置
			ai_settings.initialize_dynamic_settings()
			create_fleet(ai_settings, screen, ship, aliens)
			ship.center_ship()

			#隐藏光标
			pygame.mouse.set_visible(False)
			#清空分数
			sb.prep_score()
			sb.prep_level()
			sb.prep_ships()


def fire_bullet(ai_settings, screen, ship, bullets):
	"""创建子弹"""
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb):
	"""响应按键和鼠标事件"""

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		check_keydown_events(event, ai_settings, screen, ship, bullets)
		check_keyup_events(event, ship)
		check_play_button(ai_settings, screen, ship, aliens, bullets, event, stats, play_button, sb)



def update_screen(ai_setting, screen, ship, bullets, aliens, stats, play_button, sb):

	    #设置绘制屏幕的颜色
        screen.fill(ai_setting.bg_color)

        #绘制飞船
        ship.blitme()

        #绘制外星人
        aliens.draw(screen)

        #绘制子弹
        for bullet in bullets.sprites():
        	bullet.draw_bullet()
        # bullets.draw(screen) #行不通，可能spire中没有此函数

        if not stats.game_active:
        	play_button.draw_button()

        #显示屏幕得分,最高分，等级
        sb.show_score()
        #让最近绘制的屏幕显示
        pygame.display.flip()
        
        #必须休眠，不然卡死
        time.sleep(0.01)

def update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sb):
	"""更新子弹位置，删除消失的子弹"""
	bullets.update()

	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#检查子弹和外星人的碰撞，当没有外星人时，从新创建一堆外星人
	check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb)

def get_number_aliens_x( ai_settings, screen ):
	"""获得x方向可创建外星人数量"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int( available_space_x / ( 2 * alien_width ))
	return number_aliens_x

def get_number_aliens_y( ai_settings, screen, ship_height ):
	"""获得y方向可创建外星人数量"""
	alien = Alien(ai_settings, screen)
	alien_height = alien.rect.height
	available_space_y = ai_settings.screen_height - 3 * alien_height -ship_height
	number_aliens_y = int( available_space_y / ( 2 * alien_height ))
	return number_aliens_y

def create_alien(ai_settings, screen, aliens, alien_number_x, alien_number_y):
		"""在当前行创建第alien_number个外星人，并加入aliens编组中"""
		alien = Alien( ai_settings, screen )
		alien.x = alien.rect.width + 2 * alien.rect.width * alien_number_x
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * alien_number_y
		aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
	"""创建外星人群"""
	number_aliens_x = get_number_aliens_x(ai_settings, screen)
	number_aliens_y = get_number_aliens_y(ai_settings, screen, ship.rect.height)
	#创建外星人群
	for alien_number_x in range( number_aliens_x ):
		for alien_number_y in range(number_aliens_y):
			create_alien(ai_settings, screen, aliens, alien_number_x, alien_number_y)

def update_ship(ship):
	"""更新飞船位置"""
	ship.update()


def check_fleet_edges(ai_settings, aliens):
	"""检查是否有外星人到边缘，到边缘则改变方向"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""改变移动方向，并向下移动"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.alien_speedy_factor
	ai_settings.alien_fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb):
	"""更新外星人位置"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	#检查外星人碰撞，并做碰撞处理
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
	#检查外星人是否触底
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb):
	"""检查子弹和外星人的碰撞，当没有外星人时，从新创建一堆外星人"""
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	#击中所有外星人后，从新创建外星人
	if len(aliens) == 0:
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings, screen, ship, aliens)

		#提高等级
		stats.level += 1
		sb.prep_level()

	if collisions:
		for alien in collisions.values():
			stats.score += ai_settings.alien_point * len(alien)
			sb.prep_score()
		check_high_score(stats, sb)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
	"""响应外星人撞击事件"""
	if stats.ship_left > 1:
		stats.ship_left -= 1

		aliens.empty()
		bullets.empty()

		#创建一群新的外星人和一个飞船
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		sleep(1)
	else:
		aliens.empty()
		bullets.empty()
		ship.center_ship()
		stats.game_active = False
		#显示光标
		pygame.mouse.set_visible(True)

	#更新飞船数量
	sb.prep_ships()

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
	"""检查外星人是否到屏幕底端"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
			break

def check_high_score(stats, sb):
	if stats.score > stats.hight_score:
		stats.hight_score = stats.score
		sb.prep_hight_score()
		
