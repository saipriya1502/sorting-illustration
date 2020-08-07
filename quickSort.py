import pygame
import time

c=[135,206,235]

def swap(i,j,array,window):
	l=array[i]
	array[i]=array[j]
	array[j]=l
	pygame.draw.line(window,(255,255,255),(i*10+100,500),(i*10+100,0),5)
	pygame.draw.line(window,c,(i*10+100,500),(i*10+100,500-array[i]),5)
	pygame.draw.line(window,(255,255,255),(j*10+100,500),(j*10+100,0),5)
	pygame.draw.line(window,c,(j*10+100,500),(j*10+100,500-array[j]),5)
	pygame.display.update()

def partition(array,start,end,window,pause,speed,delay):
	pivot=array[end]
	low=start-1
	for i in range(start,end):
		delay=0.05-speed.val
		if array[i]<pivot:
			low+=1
			swap(low,i,array,window)
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
	swap(low+1,end,array,window)
	return low+1

def quicksort(array,start,end,window,pause,speed,delay):
	if start<end:
		pi=partition(array,start,end,window,pause,speed,delay)
		quicksort(array,start,pi-1,window,pause,speed,delay)
		quicksort(array,pi+1,end,window,pause,speed,delay)


def quickSort(array,start,end,window,pause,speed,delay):
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
	speed.draw()
	quicksort(array,start,end,window,pause,speed,delay)