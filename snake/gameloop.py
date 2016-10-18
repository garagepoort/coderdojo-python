#!/usr/bin/python
import sys
from snake import *
from gamelogic import *
from gameDrawer import *
from time import sleep

global running
global gamelogic
global gameDrawer

running = True;
gameLogic = Gamelogic();
gameDrawer = GameDrawer();


window = GraphWin('Snake', 400, 300, autoflush=False)


gameDrawer.draw(window, gameLogic)

while running == True:
	gameLogic.execute(window)
	gameLogic.getSnake().move()
	gameDrawer.draw(window, gameLogic)
	window.update()
	sleep(0.20)