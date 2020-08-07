import pygame
import time
c=[135,206,235]
def merge(array,start,mid,end,window,pause,speed):
	delay=0.05-speed.val
	first=mid-start+1
	second=end-mid
	i=j=0
	k=start
	L=[array[start+i] for i in range(first)]
	R=[array[mid+1+i] for i in range(second)]
	while i<first and j<second:
		if L[i]>R[j]:
			array[k]=R[j]	
			j+=1
		else:
			array[k]=L[i]
			i+=1
		k+=1
		
	while i<first:
		array[k]=L[i]
		i+=1
		k+=1
	while j<second:
		array[k]=R[j]
		j+=1
		k+=1
	j=start
	for i in range(start*10,end*10+1,10):
		pygame.draw.line(window,(255,255,255),(i+100,500),(i+100,0),5)
		pygame.draw.line(window,c,(i+100,500),(i+100,500-array[i//10]),5)
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
def mergesort(array,start,end,window,pause,speed):
	if start<end:
		mid=start+(end-start)//2
		mergesort(array,start,mid,window,pause,speed)
		mergesort(array,mid+1,end,window,pause,speed)
		merge(array,start,mid,end,window,pause,speed)
		
def mergeSort(array,start,end,window,pause,speed):
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
	mergesort(array,start,end,window,pause,speed)

