import driver
import traffic
import pygame
from pygame.locals import *
import gameSetup
import background


def main():
	pygame.init()
	gamedisplay=pygame.display.set_mode((840,650))
	print("#testing driver car model#")
	test_driver=driver.Driver(0,0)

	print("#right input test#")
	test_driver.moveRight()
	assert test_driver.x==5

	print('#zero input test#')
	assert test_driver.x==5

	print('#left input test#')
	test_driver.moveLeft()
	assert test_driver.x==0

	print("#testing traffic model#")
	test_traffic=traffic.Traffic(0)

	print('#speedup test#')
	oldspeed=test_traffic.randomspeed
	test_traffic.speedup()
	assert test_traffic.randomspeed>oldspeed

	print('#slowdown test#')
	oldspeed=test_traffic.randomspeed
	test_traffic.slowdown()
	assert test_traffic.randomspeed<oldspeed

	print('#reset test#')
	test_traffic.reset()
	assert test_traffic.y>=-2000 and test_traffic.y<=-500

	print('#drive test#')
	test_traffic.drive()
	assert test_traffic.y>=-2000 and test_traffic.y<=-500

	print('#testing gameSetup model#')
	test_gameSetup=gameSetup.GameSetup()

	print('#game screen test#')
	test_gameSetup.setup()
	assert test_gameSetup.display_width==840

	print('#testing background model#')
	test_background=background.Background()

	print('#testing reset#')
	test_background.reset()
	assert test_background.y==-650

	print('#testing speedup#')
	test_background.speedup()
	assert test_background.speed<=5

	print('#testing slowdown#')
	test_background.slowdown()
	assert test_background.speed>=2

main()
