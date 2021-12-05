import pygame
import os
import sys

from main import mainRun
from sudoku_gui import main

  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (612,408) 
# opens up the window 
screen = pygame.display.set_mode(res) 
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (0,0,0)


#Back-ground Image
bg = pygame.image.load(r'bg.jpg')


width = screen.get_width()  
height = screen.get_height() 
smallfont = pygame.font.SysFont('Raleway Bold',35) 

text_play = smallfont.render('Play!' , True , color)
text_solve = smallfont.render('Solve' , True , color)
text = smallfont.render('Quit' , True , color) 

  
while True: 
      
    for ev in pygame.event.get(): 
        
        # if ev.type == pygame.MOUSEBUTTONDOWN:
            
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
            #if the mouse is clicked on the 
            #button the game is terminated 
            if width/2 <= mouse[0] <= (width/2)+140 and height/2 <= mouse[1] <= (height/2)+40: 
                pygame.quit()
            
            if width/2 <= mouse[0] <= width/2+140 and (height/2)-50 <= mouse[1] <= height/2+40-50:
                # os.system('main.py')
                mainRun()
            
            if width/2 <= mouse[0] <= width/2+140 and (height/2)-100 <= mouse[1] <= height/2+40-100:
                main()


        
                  
    # fills the screen with a color 
    screen.fill((60,25,60)) 
    #image is added
    screen.blit(bg, (0, 0))
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])   
    screen.blit(text , ((width/2),height/2)) 


    if width/2 <= mouse[0] <= width/2+140 and (height/2)-100 <= mouse[1] <= height/2+40-100: 
        pygame.draw.rect(screen,color_light,[width/2,(height/2)-100,140,40]) 
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,(height/2-100),140,40])
    screen.blit(text_play, ((width/2),(height/2)-100))

    if width/2 <= mouse[0] <= width/2+140 and (height/2)-50 <= mouse[1] <= height/2+40-50: 
        pygame.draw.rect(screen,color_light,[width/2,(height/2)-50,140,40]) 
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,(height/2-50),140,40])
    screen.blit(text_solve, ((width/2),(height/2)-50))


    pygame.display.update()