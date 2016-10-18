#!/usr/bin/python
import sys
from snake import *
from gamelogic import *
from gameDrawer import *
from world import *
from time import sleep

window = GraphWin('Snake', 400, 300, autoflush=False)

running = True;
gameLogic = Gamelogic();
world = World()
gameDrawer = GameDrawer(window);

gameDrawer.draw(world)

while running == True and world.isGameOver() == False:
	gameLogic.execute(window, world)
	world.getSnake().move()
	gameDrawer.draw(world)
	window.update()
	sleep(0.20)