import pygame
from time import gmtime, strftime
import time

# constants
noImages = 11
showtimeImage = 10

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((320,240), 0, 32)

# set up the colors
GREY = (200, 200, 200)

# set up fonts
timeFont = pygame.font.SysFont(None, 32)
dateFont = pygame.font.SysFont(None, 32)
myimage = pygame.image.load('im1.jpg')
# counting the seconds when to change image
secondsPassed = 0
# image index
imageIndex = 1
while True:
	# getting date and time
	mydate = strftime("%Y-%m-%d")
	mytime = strftime("%H:%M:%S")
	
	# set up the text
	textTime = timeFont.render(mytime, True, GREY)
	textDate = dateFont.render(mydate, True, GREY)

	rectDate = textDate.get_rect()
	rectDate.centerx = windowSurface.get_rect().centerx - 100
	rectDate.centery = windowSurface.get_rect().centery + 105	
	
	rectTime = textTime.get_rect()
	rectTime.centerx = windowSurface.get_rect().centerx + 100
	rectTime.centery = windowSurface.get_rect().centery + 105	
	
	# fill the background with black
	windowSurface.fill((0, 0, 0))

	# draw the text onto the surface
	windowSurface.blit(myimage, (0,0))
	windowSurface.blit(textTime, rectTime)
	windowSurface.blit(textDate, rectDate)
	if (secondsPassed == showtimeImage):
		myimage = pygame.image.load('images/im'+str(imageIndex)+'.jpg')
		secondsPassed = 0
		imageIndex = imageIndex + 1
		if (imageIndex > noImages):
			imageIndex = 1
	
	
	# draw the window onto the screen
	pygame.display.update()

	# sleep one second
	time.sleep(1)
	secondsPassed = secondsPassed + 1 
