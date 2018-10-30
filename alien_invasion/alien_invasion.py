# coding=utf-8

import threading
import settings
import pygame
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    """初始化游戏创建一个屏幕对象"""
    
    print('thread %s is running...' % threading.current_thread().name)
    pygame.init()
    ai_setting  = settings.Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, 
                                        ai_setting.screen_height) )
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_setting.ship_speed_factor, screen)
  
    #创建存储子弹的编组
    bullets = Group()
    #创建外星人群
    aliens = Group()
    gf.create_fleet(ai_setting, screen, ship, aliens)
    #创建统计信息
    stats = GameStats(ai_setting)
    #创建play按钮
    play_button = Button(ai_setting, screen, "play")
    #创建统计游戏得分的实例
    sb = Scoreboard(ai_setting, screen, stats)


    while(True):
        gf.check_events(ai_setting, screen, ship, aliens, bullets, stats, play_button, sb)
        #当前游戏处于激活状态
        if stats.game_active:
            gf.update_ship(ship)
            gf.update_bullets(ai_setting, screen, ship, bullets, aliens, stats, sb)
            gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets, sb)
            
        gf.update_screen(ai_setting, screen, ship, bullets, aliens, stats, play_button, sb)
                            


def main():
    """主函数开启线程运行游戏"""
    
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=run_game, name = "game_thread")
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
    
#启动主程序
main()
