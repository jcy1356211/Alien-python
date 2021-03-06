import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats 
def run_game():
	pygame.init()#初始化背景设置
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)

	#创建一艘飞船、一个子弹编组和一个外星人编组
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()

	#创建外星人群
	gf.create_fleet(ai_settings,screen,aliens,ship)

	#开始游戏的主循环
	while True:
		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)
		#每次循环时都重绘屏幕		
		if stats.game_active:
			ship.update()
			#每次循环时更新子弹的位置，并删除消失的子弹
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
			#更新每个外星人的位置
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets) 
			#每次循环时都更新屏幕
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
run_game() 