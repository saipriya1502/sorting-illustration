import pygame
import time
import button
from slider import Slider
c=[135,206,235]

def swap(array,i,j,window):
	l=array[i]
	array[i]=array[j]
	array[j]=l
	pygame.draw.line(window,(255,255,255),(i*10+100,500),(i*10+100,0),5)
	pygame.draw.line(window,c,(i*10+100,500),(i*10+100,500-array[i]),5)
	pygame.draw.line(window,(255,255,255),(j*10+100,500),(j*10+100,0),5)
	pygame.draw.line(window,c,(j*10+100,500),(j*10+100,500-array[j]),5)
	pygame.display.update()

def bubbleSort(array,window,pause,speed):
	k=len(array)
	delay=0.025
	run=True
	while run:
		for event in pygame.event.get():
			if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and pause.isOver(pygame.mouse.get_pos()):
				run=False
			elif event.type==pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
				pos = pygame.mouse.get_pos()
				if speed.button_rect.collidepoint(pos):
					speed.hit = True
					break
			elif event.type == pygame.MOUSEBUTTONUP:
				speed.hit = False
				break
		if speed.hit:
			speed.move()
			delay=0.05-speed.val
		speed.draw()
		pygame.display.flip()
	while k>1:
		for i in range(1,k):
			if array[i-1]>array[i]:
				swap(array,i-1,i,window)
			speed.draw()
			for event in pygame.event.get():
				if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and pause.isOver(pygame.mouse.get_pos()):
					run=True
					while run:
						for event in pygame.event.get():
							if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and pause.isOver(pygame.mouse.get_pos()):
								run=False
							elif event.type==pygame.QUIT:
								pygame.quit()
							elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
								pos = pygame.mouse.get_pos()
								if speed.button_rect.collidepoint(pos):
									speed.hit = True
									break
							elif event.type == pygame.MOUSEBUTTONUP:
								speed.hit = False
								break
						if speed.hit:
							speed.move()
							delay=0.05-speed.val
						speed.draw()
						pygame.display.flip()
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
					pos = pygame.mouse.get_pos()
					if speed.button_rect.collidepoint(pos):
						speed.hit = True
						break
				elif event.type==pygame.QUIT:
					pygame.quit()
				elif event.type == pygame.MOUSEBUTTONUP:
					speed.hit = False
					break

			if speed.hit:
				speed.move()
				delay=0.05-speed.val
			speed.draw()
			pygame.display.flip()
			time.sleep(delay)
		k-=1;

		
