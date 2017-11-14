#this doesn't do anything yet but if it doesn't return any errors it should work i think - Ramon

import sys, pygame, random
pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = [0, 0, 0]
white = [255, 255, 255]

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

myfont = pygame.font.SysFont("monospace", 15)
pygame.display.set_icon(pygame.image.load("Assets/ball.png"))
pygame.display.set_caption("Uranus invaders")


screen.fill(white)

class GameMenu() :
    def __init__(self, screen, items):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.clock = pygame.time.Clock()
        self.items = []
        self.font = myfont

        for index, item in enumerate(items):
            label = self.font.render(item, 1, white)
 
            width = label.get_rect().width
            height = label.get_rect().height
 
            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
            #sets label properties in an array
            self.items.append([item, [label, (width, height), (posx, posy)]])

    def run(self) :
        running = True
        while running:
            for name, labelProperties in self.items:
                #reads label properties from  the array set in the __INIT__
                label = labelProperties[0]
                posx = labelProperties[2][0]
                posy = labelProperties[2][1]
                self.screen.blit(label, (posx, posy))

            for i in pygame.event.get():
                print(i);
                print("Type:"  + str(i.type))
                if hasattr(i, "key"):
                    print("key:"  + str(getattr(i, "key")))

                if i.type == pygame.QUIT or (hasattr(i, "key") and getattr(i, "key") == 27):
                    running = False
                    pygame.quit()
                else:
                    #sets the fps and updates the game screen.
                    pygame.display.update()
                    self.clock.tick(30)

if __name__ == "__main__":
    # Creating the screen
    screen = pygame.display.set_mode(size)
    menuItems = ('Start', 'Quit')
    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen, menuItems)
    gm.run()