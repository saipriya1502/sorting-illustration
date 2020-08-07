import pygame
import time
c=[135,206,235]
def selection(array,start,end,window,pause,speed):
	delay=0.05-speed.val
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
	for i in range(start,end):
		l=array[i]
		for j in range(i+1,end+1):
			if(array[j]<l):
				k=j
				l=array[j]
				time.sleep(delay)
		if(not(l==array[i])):
			pygame.draw.line(window,(255,255,255),(k*10+100,500),(k*10+100,0),5)
			pygame.draw.line(window,c,(k*10+100,500),(k*10+100,500-array[i]),5)
			pygame.draw.line(window,(255,255,255),(i*10+100,500),(i*10+100,0),5)
			pygame.draw.line(window,c,(i*10+100,500),(i*10+100,500-l),5)
			array[k]=array[i]
			array[i]=l
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

			if speed.hit:
				speed.move()
				delay=0.05-speed.val
			speed.draw()
			pygame.display.flip()
			time.sleep(delay)
