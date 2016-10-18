#!/usr/bin/python
import sys
from snake import *
from gamelogic import *
from gameDrawer import *
from world import *
from time import sleep

running = True;
gameLogic = Gamelogic();
gameDrawer = GameDrawer();
world = World()

window = GraphWin('Snake', 400, 300, autoflush=False)

gameDrawer.draw(window, world)

while running == True and world.isGameOver() == False:
	gameLogic.execute(window, world)
	world.getSnake().move()
	gameDrawer.draw(window, world)
	window.update()
	sleep(0.20)