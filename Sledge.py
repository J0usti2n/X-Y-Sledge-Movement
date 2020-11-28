import pygame
import random
import time

#_Classes________________________________________________________________
class Settings(object):
    #-screen---------------------
    size    = [700, 500]
    screen  = pygame.display.set_mode(size)
    clock   = pygame.time.Clock()
    done    = False
    #-Colors---------------------
    white       = (255, 255, 255)
    black       = (0, 0, 0)
    green       = (0, 255, 0)
    mid_green   = (60, 140, 0)
    dark_Green  = (0, 100, 0)
    red         = (255, 0, 0)
    brown       = (169,72,23)

#_Sledge_________________________________________________________________
class Sledge(Settings):
    def __init__(self, px, py, pscreen):
        super().__init__()
        self.x      = px
        self.y      = py
        self.hit    = False
        self.screen = pscreen
    #-Draw------------------------
    def draw(self):
        pygame.draw.rect(Settings.screen, Settings.brown, [self.x, self.y, 5, 75])
        pygame.draw.rect(Settings.screen, Settings.brown, [self.x+35, self.y, 5, 75])
        pygame.draw.rect(Settings.screen, Settings.red, [self.x+5, self.y+15, 30, 50])
    #-Movement--------------------
    # X-axis
    def move_left(self):
        if self.x > 0:
            self.x -= 5
            print("Moving Left")
    def move_right(self):
        if self.x < Settings.screen.get_width()-55:
            self.x += 5
            print("Moving Right")
    # Y-axis
    def move_up(self):
        if self.y > 0:
            self.y -= 5
            print("Moving Up")
    def move_down(self):
        if self.y < self.screen.get_width()-55:
            self.y += 5
            print("Moving Down")

    def hit(self):
        self.hit = True
#_Game__________________________________________________________
class Game(Settings):
    def __init__(self):
        super().__init__()
        self.done   = False
        self.player = Sledge(350, 400, Settings.screen)
        self.paused = False
        
    #-Main-Loop--------------------------------
    def main_loop(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            key    = pygame.key.get_pressed()                                   # important to check if a key is pressed

            if self.player.hit == False:                                        # as long as the player isn't hitted the programm continues
                Settings.screen.fill(Settings.white)                            # setting background White
                Settings.clock.tick(60)                                         # lock the FPS on 60
                
                #-draw-commands--------------------------------------------------
                self.player.draw()                                              

                if self.paused != True:                                         # if the game is not paused, the Movement is available
                    #-X-keys-----------------------------------------------------
                    if key[pygame.K_LEFT] or key[pygame.K_a] == True:
                        self.player.move_left()     
                    elif key[pygame.K_RIGHT] or key[pygame.K_d] == True:
                        self.player.move_right()
                    #-Y-keys-----------------------------------------------------
                    elif key[pygame.K_UP] or key[pygame.K_w] == True:
                        self.player.move_up()
                    elif key[pygame.K_DOWN] or key[pygame.K_s] == True:
                        self.player.move_down()
                #-Pause-keys-----------------------------------------------------
                    elif key[pygame.K_p] == True:
                        print("paused")
                        self.paused = True   
                elif key[pygame.K_u] == True:
                    print("unpaused")
                    self.paused = False
                #-Quit-game-------------------------------------------------------
                elif key[pygame.K_ESCAPE] == True:
                    pygame.quit()
            #-Update-screen-------------------------------------------------------
            pygame.display.flip()           


game = Game()
game.main_loop()