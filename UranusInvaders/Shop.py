from utils import utils, MenuItem
class Shop(object):
    def __init__(self, pyg, screen):
        self.pyg = pyg
        self.screen = screen
        self.currency = utils.loadObject("Currency")
        self.screenWidth = pyg.display.Info().current_w
        self.screenHeight = pyg.display.Info().current_h

    def background(self):

        currency = MenuItem("£" + str(self.currency), "none")
        currency.set_position(20, 20)
        currency.set_font_color((33,108,42))
        self.screen.blit(currency.label, currency.position)

        shop = MenuItem("Shop", "none")
        shop.set_position((self.screenWidth / 2) - (shop.width / 2), 50)
        shop.set_font_color((255, 0, 0))
        self.screen.blit(shop.label, shop.position)

        speed = MenuItem("Spaceship Speed", "none")
        speed.set_position(50, 100)
        speed.set_font_color((255, 0, 0))
        self.screen.blit(speed.label, speed.position)

        rect = self.pyg.Rect(speed.pos_x + speed.width + 50, speed.pos_y - 15, 300, 50)
        self.pyg.draw.rect(self.screen, (255, 0, 0), rect, 2)



    def run(self, event):
        m = "k"