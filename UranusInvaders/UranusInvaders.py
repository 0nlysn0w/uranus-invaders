#this doesn't do anything yet but if it doesn't return any errors it should work i think - Ramon

import sys, pygame, random
from BaseRenderer import BaseRenderer
pygame.init()


myfont = pygame.font.SysFont("monospace", 15)
pygame.display.set_icon(pygame.image.load("Assets/ball.png"))
pygame.display.set_caption("Uranus invaders")


if __name__ == "__main__":
    # Creating the screen
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    
    #sets the initial value to make sure it runs the main menu
    state = "main"

    baseRenderer = BaseRenderer(pygame, screen)
    #the true is because if the state is quit python quits
    while True:
        #sets state to main after the called function has finished to return you to the main menu
        if state == "tim":
            print(state)
            state = "main"
        elif state == "ramon":
            baseRenderer.run("Asteroids", "Asteroids")
            print(state)
            state = "main"
        elif state == "joost":
            print(state)
            state = "main"
        elif state == "jurian":
            baseRenderer.run("PlanetarySurvival", "PlanetarySurvival")
            print(state)
            state = "main"
        elif state == "floris":
            print(state)
            state = "main"
        elif state == "kelvin":
            baseRenderer.run("TrafficMadness", "TrafficMadness")
            print(state)
            state = "main"
        elif state == "main":
            state = baseRenderer.run("GameMenu", "GameMenu")
        else:
            #if the state is quit or anything that isn't specified above the game will quit
            pygame.quit()
            quit()
