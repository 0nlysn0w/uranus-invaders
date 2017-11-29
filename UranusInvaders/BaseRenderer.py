import sys
from Asteroids import Asteroids

class BaseRenderer():
    def __init__(self, pyg, screen):
        print("base")
        self.clock = pyg.time.Clock()
        self.pyg = pyg
        self.screen = screen
    
    def run(self, fileName, className):
        running = True

        model = __import__(fileName)
        classToCall = getattr(model, className)
        classCalled = classToCall(self.pyg, self.screen);
        while running:

            
            for i in self.pyg.event.get():
                #Sets the screen to standard black
                self.screen.fill((0, 0, 0))

                #This makes sure the init function works, if you don't want to call the run function, that's your loss
                
                state = classCalled.run()
                if type(state) == str:
                    state,value = state.split("=")
                    if state == "return":
                        return value

                if i.type == self.pyg.QUIT or (hasattr(i, "key") and self.pyg.KEYDOWN == i.type and getattr(i, "key") == 27):
                    running = False
                    return "quit";
                else:
                    #sets the fps and updates the game screen.
                    self.pyg.display.update()
                    self.clock.tick(30)


