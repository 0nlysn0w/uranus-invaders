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
    #screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    screen = pygame.display.set_mode(size)

    #sets the initial value to make sure it runs the main menu
    state = "main"
    pygame.key.set_repeat(1, 10)
    baseRenderer = BaseRenderer(pygame, screen)
    #the true is because if the state is quit python quits
    while True:
        #sets state to main after the called function has finished to return you to the main menu
        print("State=" + state)
        if state == "tim":
            baseRenderer.run("SpaceInvaders", "SpaceInvaders")
            state = "main"
        elif state == "ramon":
            baseRenderer.run("Asteroids", "Asteroids")
            state = "main"
        elif state == "joost":
            baseRenderer.run("SpaceRace", "SpaceRace")
            state = "main"
        elif state == "jurian":
            baseRenderer.run("PlanetarySurvival", "PlanetarySurvival")
            state = "main"
        elif state == "floris":
            baseRenderer.run("AlienSlayer", "AlienSlayer")
            state = "main"
        elif state == "kelvin":
            baseRenderer.run("TrafficMadness", "TrafficMadness")
            state = "main"
        elif state == "main":
            state = baseRenderer.run("GameMenu", "GameMenu")
        else:
            #if the state is quit or anything that isn't specified above the game will quit
            pygame.quit()
            quit()
