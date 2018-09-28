#!/usr/bin/python
import sys
from snake import *
from gamelogic import *
from gameDrawer import *
from world import *
from time import sleep

window = GraphWin('Snake', 420, 330, autoflush=False)

running = True
gameLogic = GameLogic()
world = World()
gameDrawer = GameDrawer(window)

gameDrawer.draw(world)
gameDrawer.draw_borders(world)

while running == True and world.is_game_over() == False and window.isClosed() == False:
	gameLogic.execute(window, world)
	world.get_snake().move()
	gameDrawer.draw(world)
	window.update()
	sleep(0.20)