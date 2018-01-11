import pygame

import constants

from GameMenu import MenuItem

GRASS_LEFT            = (0, 32, 32, 32)
GRASS_RIGHT           = (0, 64, 32, 32)
GRASS_MIDDLE          = (0, 0, 32, 32)
DIRT_LEFT            = (0, 128, 32, 32)
DIRT_RIGHT           = (0, 160, 32, 32)
DIRT_MIDDLE          = (0, 96, 32, 32)
STONE_PLATFORM_LEFT   = (128, 32, 32, 32)
STONE_PLATFORM_MIDDLE = (128, 0, 32, 32)
STONE_PLATFORM_RIGHT  = (128, 64, 32, 32)

class PlanetarySurvival():
    def __init__(self, pyg, screen):
        #Hier kan je plaatjes inladen en in self.{NAAM} zetten en in de run functie dan weer gebruiken, dit zorgt ervoor dat je tijdens het spelen niets hoeft in te laden
        print("init planetary survival")
        self.pyg = pyg
        self.screen = screen
        self.screenWidth = pyg.display.Info().current_w
        self.screenHeight = pyg.display.Info().current_h
        self.image = pyg.image.load("Assets/Wheatley.png")
        self.items = []
        self.rect = self.image.get_rect()
        self.width = self.rect.size[0]
        self.height = self.rect.size[1]
        self.x = (self.screenWidth - self.width)/2
        self.y = (self.screenHeight - self.height)/2

        items = ("Start", "How to play", "Quit")
        redir = ("game", "htp", "quit")
        for index, item in enumerate(items):
            menu_item = MenuItem(item, redir[index])

            t_h = len(items) * menu_item.height
            pos_x = (self.screenWidth / 2) - (menu_item.width / 2)
            pos_y = (self.screenHeight / 2) - (t_h / 2) + ((index * 2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

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

        # Import the levels
        levels = Level(player)

        # Create all the levels
        level_list = []
        level_list.append(Level_01(player))
        level_list.append(Level_02(player))

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

    def menu(self):
        for item in self.items:
            mouseProperties = self.pyg.mouse.get_pos()
            if item.is_mouse_selection(mouseProperties[0], mouseProperties[1]):
                item.set_font_color((255, 0, 0))
                item.set_italic(True)
                if self.pyg.mouse.get_pressed()[0]:
                    self.state = item.redir

            else:
                item.set_font_color((255, 255, 255))
                item.set_italic(False)
            self.screen.blit(item.label, item.position)

    def gameover(self):
            gameover = MenuItem("Game over!", "none", None, 80, (138, 7, 7))
            pos_x = (self.screenWidth / 2) - (gameover.width / 2)
            pos_y = (self.screenHeight / 2) - (gameover.height / 2)
            gameover.set_position(pos_x, pos_y)
            self.screen.blit(gameover.label, gameover.position)

            tryagain = MenuItem("Try again", "tryagain", None, 30, (255, 255, 255))
            pos_x = (self.screenWidth / 4 ) - (tryagain.width / 2)
            pos_y = (self.screenHeight / 8 * 6) - (tryagain.height / 2)
            tryagain.set_position(pos_x, pos_y)

            quit = MenuItem("Quit", "quit", None, 30, (255, 255, 255))
            pos_x = (self.screenWidth / 4 * 3) - (quit.width / 2)
            pos_y = (self.screenHeight / 8 * 6) - (quit.height / 2)
            quit.set_position(pos_x, pos_y)
            items = []
            items.append(tryagain)
            items.append(quit)
            for item in items:
                mouseProperties = self.pyg.mouse.get_pos()
                if item.is_mouse_selection(mouseProperties[0], mouseProperties[1]):
                    item.set_font_color((255, 0, 0))
                    item.set_italic(True)
                    if self.pyg.mouse.get_pressed()[0]:
                        print("left clicked")
                        print(item.redir)
                        if item.redir == "tryagain":
                            return "tryagain"
                        if item.redir == "quit":
                            return "quit"

                else:
                    item.set_font_color((255, 255, 255))
                    item.set_italic(False)
                self.screen.blit(item.label, item.position)

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        sprite_sheet = SpriteSheet("Assets/spritesheet-0002.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()


        self.image = pygame.image.load("Assets/spaceship-0002.png")
        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """

    def __init__(self, sprite_sheet_data):

        super().__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """


        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1


class MovingEnemy(Enemy):
    """ This is a fancier platform that can actually move. """

    def __init__(self, sprite_sheet_data):

        super().__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None
        self.flipped = False

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """


        # Move left/right
        self.rect.x += self.change_x
        if self.change_x == -1 and self.flipped == False:
            self.image = pygame.transform.rotate( self.image, 180)
            self.flipped = True

        if self.change_x == 1 and self.flipped == True:
            self.flipped = False
            self.image = pygame.transform.rotate( self.image, 180)

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit

            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            print('hello hit very hard on top or ondertop')
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """


    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # -- Attributes
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []

        # What direction is the player facing?
        self.direction = "R"

        # List of sprites we can bump against
        self.level = None

        sprite_sheet = SpriteSheet("Assets/player-0001-walk-right.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(192, 0, 32, 64)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(160, 0, 32, 64)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(128, 0, 32, 64)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(96, 0, 32, 64)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(64, 0, 32, 64)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(32, 0, 32, 64)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 0, 32, 64)
        self.walking_frames_r.append(image)

        # Load all the right facing images
        sprite_sheet2 = SpriteSheet("Assets/player-0001-walk-left.png")
        # Load all the right facing images into a list
        image = sprite_sheet2.get_image(0, 0, 32, 64)
        self.walking_frames_l.append(image)
        image = sprite_sheet2.get_image(32, 0, 32, 64)
        self.walking_frames_l.append(image)
        image = sprite_sheet2.get_image(64, 0, 32, 64)
        self.walking_frames_l.append(image)
        image = sprite_sheet2.get_image(96, 0, 32, 64)
        self.walking_frames_l.append(image)
        image = sprite_sheet2.get_image(128, 0, 32, 64)
        self.walking_frames_l.append(image)
        image = sprite_sheet2.get_image(160, 0, 32, 64)
        self.walking_frames_l.append(image)
        image = sprite_sheet2.get_image(192, 0, 32, 64)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .4

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -3
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 3
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None
        self.enemy_list = None

        # Background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))


        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Assets/background-space-0001.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [DIRT_LEFT, 400, 550],
                  [DIRT_MIDDLE, 400, 518],
                  [DIRT_MIDDLE, 400, 486],
                  [DIRT_MIDDLE, 400, 454],
                  [DIRT_MIDDLE, 400, 422],
                  [DIRT_MIDDLE, 400, 390],
                  [DIRT_MIDDLE, 400, 358],
                  [DIRT_MIDDLE, 400, 326],
                  [DIRT_MIDDLE, 400, 294],
                  [DIRT_MIDDLE, 400, 262],
                  [DIRT_MIDDLE, 400, 230],
                  [DIRT_MIDDLE, 400, 198],
                  [DIRT_MIDDLE, 400, 166],
                  [DIRT_MIDDLE, 400, 134],
                  [DIRT_MIDDLE, 400, 102],
                  [DIRT_MIDDLE, 400, 70],
                  [DIRT_MIDDLE, 400, 38],
                  [DIRT_MIDDLE, 400, 6],
                  [GRASS_MIDDLE, 400, -26],
                  [GRASS_MIDDLE, 432, 550],
                  [GRASS_MIDDLE, 464, 550],
                  [GRASS_MIDDLE, 496, 550],
                  [GRASS_MIDDLE, 528, 550],
                  [GRASS_MIDDLE, 560, 550],
                  [GRASS_MIDDLE, 592, 550],
                  [GRASS_MIDDLE, 624, 550],
                  [GRASS_MIDDLE, 656, 550],
                  [GRASS_MIDDLE, 688, 550],
                  [GRASS_MIDDLE, 720, 550],
                  [GRASS_MIDDLE, 752, 550],
                  [GRASS_MIDDLE, 784, 550],
                  [GRASS_MIDDLE, 816, 550],
                  [GRASS_RIGHT, 848, 550],
                  [STONE_PLATFORM_LEFT, 1008, 486],
                  [STONE_PLATFORM_MIDDLE, 1040, 486],
                  [STONE_PLATFORM_RIGHT, 1072, 486],
                  [STONE_PLATFORM_LEFT, 1136, 380],
                  [STONE_PLATFORM_MIDDLE, 1168, 380],
                  [STONE_PLATFORM_RIGHT, 1200, 380],
                  [STONE_PLATFORM_LEFT, 1680, 348],
                  [STONE_PLATFORM_MIDDLE, 1712, 348],
                  [STONE_PLATFORM_RIGHT, 1744, 348],
                  [DIRT_LEFT, 1904, 550],
                  [DIRT_MIDDLE, 1904, 518],
                  [GRASS_MIDDLE, 1904, 486],
                  [GRASS_MIDDLE, 1936, 550],
                  [GRASS_MIDDLE, 1968, 550],
                  [DIRT_MIDDLE, 2000, 518],
                  [GRASS_MIDDLE, 2000, 486],
                  [DIRT_MIDDLE, 2000, 550],
                  [GRASS_MIDDLE, 2032, 550],
                  [GRASS_MIDDLE, 2064, 550],
                  [DIRT_MIDDLE, 2096, 550],
                  [DIRT_MIDDLE, 2096, 518],
                  [GRASS_MIDDLE, 2096, 486],
                  [GRASS_MIDDLE, 2128, 550],
                  [GRASS_MIDDLE, 2160, 550],
                  [DIRT_MIDDLE, 2192, 550],
                  [DIRT_MIDDLE, 2192, 518],
                  [GRASS_MIDDLE, 2192, 486],
                  [GRASS_MIDDLE, 2224, 550],
                  [GRASS_MIDDLE, 2256, 550],
                  [DIRT_MIDDLE, 2288, 550],
                  [DIRT_MIDDLE, 2288, 518],
                  [GRASS_MIDDLE, 2288, 486],
                  [GRASS_RIGHT, 2320, 550],
                  [GRASS_LEFT, 2400, 454],
                  [GRASS_MIDDLE, 2432, 454],
                  [GRASS_RIGHT, 2464, 454],
                  [GRASS_LEFT, 2600, 370],
                  [GRASS_MIDDLE, 2632, 370],
                  [GRASS_RIGHT, 2664, 370],
                  [GRASS_LEFT, 2800, 450],
                  [GRASS_MIDDLE, 2832, 450],
                  [GRASS_RIGHT, 2864, 450],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


        # Add a custom moving platform
        block = MovingPlatform(STONE_PLATFORM_MIDDLE)
        block.rect.x = 1250
        block.rect.y = 380
        block.boundary_left = 1250
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving Enemy
        block = MovingEnemy(Enemy)
        block.rect.x = 1904
        block.rect.y = 380
        block.boundary_left = 1904
        block.boundary_right = 2320
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Assets/background-space-0001.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000

        self.surface = pygame.image.load("Assets/dirt-surface-0001.png").convert()

        # Array with type of platform, and x, y location of the platform.
        level = [ [STONE_PLATFORM_LEFT, 30, 550],
                  [STONE_PLATFORM_MIDDLE, 370, 550],
                  [STONE_PLATFORM_RIGHT, 440, 550],
                  [GRASS_LEFT, 800, 400],
                  [GRASS_MIDDLE, 870, 400],
                  [GRASS_RIGHT, 940, 400],
                  [GRASS_LEFT, 1000, 500],
                  [GRASS_MIDDLE, 1070, 500],
                  [GRASS_RIGHT, 1140, 500],
                  [STONE_PLATFORM_LEFT, 1120, 280],
                  [STONE_PLATFORM_MIDDLE, 1190, 280],
                  [STONE_PLATFORM_RIGHT, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = MovingPlatform(STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(constants.BLACK)

        # Return the image
        return image
