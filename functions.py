import pygame
from pygame.locals import *
import sys
import time
import random

class Game:
    ''' Constructor'''
    def __init__(self):
        self.w = 800
        self.h = 600
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.wpm
        self.score = 0
        self.result = 'Time:0 Accuracy:0 % WPM:0 Score: 0'
        self.end = False
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)
        
def testing():
    return "in testing"

if __name__ == '__functions__':
    testing()