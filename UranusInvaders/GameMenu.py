import pygame
from utils import MenuItem

class GameMenu():
    def __init__(self, pyg, screen):
        self.pyg = pyg
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.clock = pygame.time.Clock()
        self.items = []

        #The names of the menu items, if you change this the text on screen changes
        items = ("Space Invaders", "Asteroids", "Alien Slayer", "Planetary Survival", "Traffic madness on Uranus", "Space Race", "Quit")

        #The name of the state which determines which minigame it'll load
        redir = ("tim", "ramon", "floris", "jurian", "kelvin", "joost", "quit")
        
        for index, item in enumerate(items):
            menu_item = MenuItem(item, redir[index])
 
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index * 2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

    def run(self, event):
        self.screen.fill((0, 0, 0))
        for item in self.items:
            mouseProperties = self.pyg.mouse.get_pos()
            if item.is_mouse_selection(mouseProperties[0], mouseProperties[1]):
                item.set_font_color((255, 0, 0))
                item.set_italic(True)
                if self.pyg.mouse.get_pressed()[0]:
                    print("left clicked")
                    print(item.redir)
                    state = item.redir
                    return "return=" + state
                    running = False

            else:
                item.set_font_color((255, 255, 255))
                item.set_italic(False)
            print(item.label)
            self.screen.blit(item.label, item.position)
