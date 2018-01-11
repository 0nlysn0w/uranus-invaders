import SpaceInv
class SpaceInvaders():
    def __init__(self, pyg, screen):
        #Hier kan je plaatjes inladen en in self.{NAAM} zetten en in de run functie dan weer gebruiken, dit zorgt ervoor dat je tijdens het spelen niets hoeft in te laden
        print("init SpaceInvaders")
        self.pyg = pyg
        self.screen = screen
        self.m = SpaceInv.main()

    def background(self):
        if self.m == "return=main":
            self.pyg.mouse.set_visible(True)
            return self.m

    def run(self, event):
        #events needed for things
        m = 0