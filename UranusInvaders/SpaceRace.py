class SpaceRace():
    def __init__(self, pyg, screen):
        #Hier kan je plaatjes inladen en in self.{NAAM} zetten en in de run functie dan weer gebruiken, dit zorgt ervoor dat je tijdens het spelen niets hoeft in te laden
        print("init SpaceRace")
        self.pyg = pyg
        self.myfont = self.pyg.font.SysFont("monospace", 30)
        self.screen = screen
        self.spaceship = pyg.image.load("Assets/spaceship-basic.png")
        self.track = pyg.image.load("Assets/track-1.png")
        self.width = pyg.display.Info().current_w
        self.height = pyg.display.Info().current_h
        self.spaceshipWidth = self.spaceship.get_rect().size[0]
        self.spaceshipHeight = self.spaceship.get_rect().size[1]
        self.spaceshipX = (self.width - self.spaceshipWidth)/2
        self.spaceshipY = (self.height - self.spaceshipHeight)/2
        self.rotation = 0

    def background(self):

        rotatedimg = self.pyg.transform.rotate(self.spaceship, self.rotation)

        self.screen.blit(self.track, (self.spaceshipX, self.spaceshipY))
        self.screen.blit(rotatedimg, ((self.width / 2) - (self.spaceshipWidth/2), (self.height / 2) - (self.spaceshipHeight/2)))

    def run(self, event):
        keys = self.pyg.key.get_pressed()

        #print(keys)

        # North
        if keys[self.pyg.K_UP] or keys[self.pyg.K_w]:
           self.spaceshipY += 5
           self.rotation = 0

        # North East
        if (keys[self.pyg.K_UP] or keys[self.pyg.K_w]) and (keys[self.pyg.K_RIGHT] or keys[self.pyg.K_d]):
            self.rotation = 315

        # East
        if keys[self.pyg.K_RIGHT] or keys[self.pyg.K_d]:
            self.spaceshipX -= 5
            self.rotation = 270

        # South East
        if (keys[self.pyg.K_RIGHT] or keys[self.pyg.K_d]) and (keys[self.pyg.K_DOWN] or keys[self.pyg.K_s]):
           self.rotation = 225

        # South
        if keys[self.pyg.K_DOWN] or keys[self.pyg.K_s]:
           self.spaceshipY -= 5
           self.rotation = 180

        # South West
        if (keys[self.pyg.K_DOWN] or keys[self.pyg.K_s]) and (keys[self.pyg.K_LEFT] or keys[self.pyg.K_a]):
           self.rotation = 135

        # West
        if keys[self.pyg.K_LEFT] or keys[self.pyg.K_a]:
            self.spaceshipX += 5
            self.rotation = 90
   
        # North West
        if (keys[self.pyg.K_LEFT] or keys[self.pyg.K_a]) and (keys[self.pyg.K_UP] or keys[self.pyg.K_w]):
           self.rotation = 45



       # self.pyg.event.pump()