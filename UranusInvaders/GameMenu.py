import pygame
myfont = pygame.font.SysFont("monospace", 15)

class GameMenu():
    def __init__(self, pyg, screen):
        self.pyg = pyg
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.clock = pygame.time.Clock()
        self.items = []
        self.font = myfont

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
            self.screen.blit(item.label, item.position)

        
class MenuItem(pygame.font.Font):
    def __init__(self, text, redir, font=None, font_size=30,
                 font_color=(255, 255, 255), pos_x = 0, pos_y = 0):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
        self.redir = redir
 
    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
 
    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)
 
    def is_mouse_selection(self, posx, posy):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False