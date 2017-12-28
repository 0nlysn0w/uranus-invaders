import sys

class BaseRenderer():
    def __init__(self, pyg, screen):
        print("base")
        self.clock = pyg.time.Clock()
        self.pyg = pyg
        self.screen = screen

    def run(self, fileName, className):
        running = True

        self.pyg.key.set_repeat(1, 10)

        model = __import__(fileName)
        classToCall = getattr(model, className)
        classCalled = classToCall(self.pyg, self.screen);
        while running:
            try:
                invert_op = getattr(classCalled, "background", None)
                if callable(invert_op):
                    self.screen.fill((0, 0, 0))
                    classCalled.background()
            except:
                pass

            for i in self.pyg.event.get():
                #TODO: delete this when done
                print("Base:  ", i)
                #Sets the screen to standard black
                state = classCalled.run(i)
                if type(state) == str:
                    state,value = state.split("=")
                    if state == "return":
                        return value

                if i.type == self.pyg.QUIT or (hasattr(i, "key") and self.pyg.KEYDOWN == i.type and getattr(i, "key") == 27):
                    try:
                        classCalled.quit()
                    except :
                        pass

                    self.pyg.key.set_repeat(0, 10)

                    running = False
                    return "quit";

            #sets the fps and updates the game screen.
            self.pyg.display.flip()
            self.clock.tick(30)
