def main():
	print("#testing driver car model#")
	test_driver=driver.Driver()

	print("#standard input test#")
	test_driver.moveright(3)
	assert test_driver.getcoordinates()==(3,0)

	print('#zero input test#')
	test_driver.moveright(0)
	assert test_driver.getcoordinates()==(3,0)

	print('#negative input test#')
	test_driver.moveright(-1)
	assert test_driver.getcoordinates()==(2,0)

	print("#testing traffic model#")
	test_traffic=traffic.Traffic()

	print('#speedup test#')
	test_traffic.speedup()
	assert test_traffic.speed>=0

	print('#slowdown test#')
	test_traffic.slowdown()
	assert test_traffic.slowdown()>=0

	print('#reset test#')
	test_traffic.reset()
	assert test_traffic.y<=-2000 and test_traffic.y>=-500

	print('#drive test#')
	test_traffic.drive()
	assert test_traffic.y<=-2000 and test_traffic.y>=-500

	print('#testing gameSetup model#')
	test_gameSetup=gameSetup.GameSetup()

	print('#game screen test#')
	test_gameSetup.setup()
	assert test_gameSetup.driver_width()==73

	print('#testing gameLoop model#')
	test_gameLoop=gameLoop.Gameloop()

	print('#testing loop#')
	test_gameLoop.loop()
	assert test_gameLoop.gamedisplay.fill==(255,255,255)

	print('#testing background model#')
	test_background=background.Background()

	print('#testing background scroll#')
	test_background.scroll()
	assert test_background.y+=test_background.speed

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
