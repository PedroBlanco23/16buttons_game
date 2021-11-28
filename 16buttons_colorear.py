import pygame
from pygame.locals import *
import os
import sys
import numpy as np
import time

#CONSTANTES
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


CELDAY, CELDAX = SCREEN_HEIGHT//4, SCREEN_WIDTH//4













def main():
    pygame.init()
    estado = np.zeros((CELDAX, CELDAY))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("16buttons_game")
    bg = 25,25,25
    screen.fill(bg)





    while True:


  
  
      screen.fill(bg)
      time.sleep(0.1)
    



      ev = pygame.event.get()
      
      for evento in ev:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 3:
          estado = np.zeros((CELDAX, CELDAY))
        if evento.type ==pygame.QUIT:
          pygame.quit()
        


      for y in range(CELDAY):
        for x in range(CELDAX):
          poly = [((x) * CELDAX, (y) * CELDAY),
          ((x+1) * CELDAX, (y) * CELDAY ),
          ((x+1) * CELDAX, (y+1) * CELDAY),
          ((x) * CELDAX, (y+1) * CELDAY)
          ]


          if estado[x, y] == 0:
            pygame.draw.polygon(screen, (128,128,128), poly, 1)
          else:
            pygame.draw.polygon(screen, (255,255,255), poly, 0)
      pygame.display.flip()

  
  
      
        
if __name__ == "__main__":
    main()