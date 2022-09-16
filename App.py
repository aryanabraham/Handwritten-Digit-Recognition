import pygame, sys
from pygame.locals import *
import numpy as np
from keras.models import load_model
import cv2

WINDOWSIZEX = 640
WINDOWSIZEY = 480

# Initialize pygame
pygame.init()

pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY))

while True: 

    for event in pygame.event.get():
        if event.type == QUIT:
              pygame.quit()
              sys.exit()
