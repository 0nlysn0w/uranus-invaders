import pygame

import constants
import levels

from player import Player

class PlanetarySurvival():
    def __init__(self, pyg, screen):
        #Hier kan je plaatjes inladen en in self.{NAAM} zetten en in de run functie dan weer gebruiken, dit zorgt ervoor dat je tijdens het spelen niets hoeft in te laden
        print("init planetary survival")
        self.pyg = pyg
        self.screen = screen
        self.wheatley = pyg.image.load("Assets/Wheatley.png")

    def background(self):
        #no events needed
        label = self.render("Planetary survival!", 1, (255,255,0))
        quit = self.render("press ESC to go back to the main menu", 1, (255,255,0))
        self.screen.blit(label, (100, 100))
        self.screen.blit(quit, (100, 500))
        self.screen.blit(self.wheatley, (300, 100))

    def run(self, event):
        """ Main Program """
        pygame.init()

        # Set the height and width of the screen
        size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Planetary Survival")

        # Create the player
        player = Player()


        # Create all the levels
        level_list = []
        level_list.append(levels.Level_01(player))
        level_list.append(levels.Level_02(player))

        # Set the current level
        current_level_no = 0
        current_level = level_list[current_level_no]

        active_sprite_list = pygame.sprite.Group()
        player.level = current_level
        player.rect.x = 640
        player.rect.y = 400
        active_sprite_list.add(player)

        #Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done = True # Flag that we are done so we exit this loop

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                    if event.key == pygame.K_UP:
                        player.jump()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        player.stop()

            # Update the player.
            active_sprite_list.update()

            # Update items in the level
            current_level.update()

            # If the player gets near the right side, shift the world left (-x)
            if player.rect.right >= 400:
                diff = player.rect.right - 400
                player.rect.right = 400
                current_level.shift_world(-diff)

            # If the player gets near the left side, shift the world right (+x)
            if player.rect.left <= 400:
                diff = 400 - player.rect.left
                player.rect.left = 400
                current_level.shift_world(diff)

            # If the player gets to the end of the level, go to the next level
            current_position = player.rect.x + current_level.world_shift
            if current_position < current_level.level_limit:
                player.rect.x = 120
                if current_level_no < len(level_list)-1:
                    current_level_no += 1
                    current_level = level_list[current_level_no]
                    player.level = current_level

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            current_level.draw(screen)
            active_sprite_list.draw(screen)

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

            # Limit to 60 frames per second
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        return "return=main"
