import pygame
import random
from button import button
from quickSort import quickSort
from mergeSort import mergeSort
from slider import Slider
from bubbleSort import bubbleSort
from insertion import insertion as insertionSort
from selection import selection as selectionSort
import time
delay=0.025
mnt=(152,251,152)

pygame.init()
window = pygame.display.set_mode((1200,600))
pygame.display.set_caption("sort")

window.fill((255,255,255))
pygame.display.update()
pygame.display.flip()

def message(msg,window):
	clearInstruction(window)
	mess=button(mnt,90,520,1000,50,msg)
	button.draw(mess,window)
def clearInstruction(window):
	pygame.draw.line(window,(255,255,255),(90,550),(1200,550),65)	
	pygame.display.update()
def clearinstruction(window,pause):
	clearInstruction(window)
	pause.draw(window)
	pygame.display.update()
def main():
	window.fill((255,255,255))
	query=[random.randrange(20,400) for i in range(100)]
	
	c=[135,206,235]
	start=100
	i=start
	j=0
	while i<1000+start:
		pygame.draw.line(window,c,(i,500),(i,500-query[j]),5)
		j+=1
		i+=10
		pygame.display.update()


	s=80
	quick=button(mnt,10+s,520,180,50,"quickSort")
	button.draw(quick,window)

	merge=button(mnt,210+s,520,180,50,"mergeSort")
	button.draw(merge,window)

	selection=button(mnt,400+s,520,200,50,"selectionSort")
	button.draw(selection,window)

	insertion=button(mnt,610+s,520,200,50,"insertionSort")
	button.draw(insertion,window)

	bubble=button(mnt,820+s,520,200,50,"bubbleSort")
	button.draw(bubble,window)

	speed = Slider("Speed", 0.025, 0.05, 0, 630)

	pygame.display.update()

	pause=button(mnt,450,520,160,50,"start/stop")
	
	run=True

	while run:
		for event in pygame.event.get():
			if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
				pos=pygame.mouse.get_pos()
				if quick.isOver(pos):
					clearinstruction(window,pause)
					#message("illustrating ..quickSort",window)
					quickSort(query,0,99,window,pause,speed,0.025)
					run=False
				elif merge.isOver(pos):
					clearinstruction(window,pause)					
					#message("illustrating ..mergeSort",window)
					mergeSort(query,0,99,window,pause,speed)
					run=False
				elif selection.isOver(pos):
					clearinstruction(window,pause)					#message("illustrating ..selectionSort",window)
					selectionSort(query,0,99,window,pause,speed)
					run=False
				elif insertion.isOver(pos):
					clearinstruction(window,pause)					#message("illustrating ..insertionSort",window)
					insertionSort(query,0,99,window,pause,speed)
					run=False
				elif bubble.isOver(pos):
					#message("illustrating ..bubbleSort",window)
					clearinstruction(window,pause)
					bubbleSort(query,window,pause,speed)
					run=False
			elif event.type==pygame.QUIT:
				pygame.quit()

	clearInstruction(window)
	restart=button(mnt,550,520,120,50,"restart")
	button.draw(restart,window)
	pygame.display.update()

	run=True
	while run:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False
				break
			if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and restart.isOver(pygame.mouse.get_pos()):
				try:
					main()
				except:
					pass
			
	pygame.quit()

if __name__=="__main__":
	try:	
		main()
	except:
		pass
