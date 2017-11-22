import sys
from Asteroids import Asteroids

class BaseRenderer():
    def __init__(self, pyg, screen):
        print("base")
        self.clock = pyg.time.Clock()
        self.pyg = pyg
        self.screen = screen
    
    def run(self, fileName, className, functionName = "run"):
        running = True
        global state
        while running:
            
            for i in self.pyg.event.get():
                #Sets the screen to standard black
                self.screen.fill((0, 0, 0))

                #Dynamically runs function from what the user input is
                
                model = __import__(fileName)
                classToCall = getattr(model, className)
                methodToCall = getattr(classToCall, functionName)
                methodToCall(self.pyg, self.screen)

                if i.type == self.pyg.QUIT or (hasattr(i, "key") and getattr(i, "key") == 27):
                    running = False
                    state = "quit"
                    return "quit";
                else:
                    #sets the fps and updates the game screen.
                    self.pyg.display.update()
                    self.clock.tick(30)


