import pygame
import time
c=[135,206,235]
def insertion(array,start,end,window,pause,speed):
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
	for i in range(start,end+1):
		value=array[i]
		hole=i
		delay=0.05-speed.val
		while(hole>0 and array[hole-1]>value):
			pygame.draw.line(window,(255,255,255),(hole*10+100,500),(hole*10+100,0),5)
			pygame.draw.line(window,c,(hole*10+100,500),(hole*10+100,500-array[hole-1]),5)
			pygame.draw.line(window,(255,255,255),((hole-1)*10+100,500),((hole-1)*10+100,0),5)
			array[hole]=array[hole-1]
			hole=hole-1
			pygame.display.update()
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
			time.sleep(delay)
		if speed.hit:
			speed.move()
			delay=0.05-speed.val
		speed.draw()
		pygame.display.flip()
		array[hole]=value
		pygame.draw.line(window,c,(hole*10+100,500),(hole*10+100,500-value),5)
		pygame.display.update()
