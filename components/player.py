import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = 3

        #animation
        self.player_idle_right = []
        self.player_idle_left = []
        self.player_run_right = []
        self.player_run_left = []
        self.player_jump_right = []
        self.player_jump_left = []
        self.player_hurt = []
        self.load_assets()
        
        self.animation_index = 0
        self.animation_direction = 'right'
        self.animation_cooldown = 50 #millis
        self.last_animation_tick = pygame.time.get_ticks()
        self.last_animation_play = self.player_idle_right[self.animation_index]

        self.image = self.player_idle_right[self.animation_index]
        self.rect = self.image.get_rect()
        self.rect.width -= 18
        self.rect.height -= 20
        self.rect.x = self.x
        self.rect.y = self.y
        self.velocity = 0
        self.hasJumped = False

    def load_assets(self):
            for i in range(1, 11): #idle animation
                img = pygame.image.load(f'assets/images/player/idle{i}.png')
                img = pygame.transform.scale(img, (self.width, self.height))
                self.player_idle_right.append(img)
                self.player_idle_left.append(pygame.transform.flip(img, True, False))

            for i in range(1, 13): #jump animation
                img = pygame.image.load(f'assets/images/player/jump{i}.png')
                img = pygame.transform.scale(img, (self.width, self.height))
                self.player_jump_right.append(img)
                self.player_jump_left.append(pygame.transform.flip(img, True, False))

            for i in range(1, 9): #hurt animation
                img = pygame.image.load(f'assets/images/player/hurt{i}.png')
                img = pygame.transform.scale(img, (self.width, self.height))
                self.player_hurt.append(img)
               
            for i in range(1, 9): #run animation
                img = pygame.image.load(f'assets/images/player/run{i}.png')
                img = pygame.transform.scale(img, (self.width, self.height))
                self.player_run_right.append(img)
                self.player_run_left.append(pygame.transform.flip(img, True, False))

    def player_border(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.rect, 2)

    def draw(self, screen):
        #offset player to adjust small collision box
        img_rect_x = self.rect.x - 13
        img_rect_y = self.rect.y - 20
        screen.blit(self.image, (img_rect_x, img_rect_y))


    def update(self, world):
        #temporary store movement change before applying
        delta_x = 0
        delta_y = 0

        current_animation = self.player_idle_right
        if self.animation_direction == 'left':
            current_animation = self.player_idle_left

        if self.hasJumped:
            if self.animation_direction == 'right':
                current_animation = self.player_jump_right
            else:
                current_animation = self.player_jump_left


        #listen key event
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.hasJumped:
            self.velocity = -15 #jump power
            self.hasJumped = True 
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            delta_x -= self.speed
            self.animation_direction = 'left'
            if not self.hasJumped:
                current_animation = self.player_run_left

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            delta_x += self.speed
            self.animation_direction = 'right'
            if not self.hasJumped:
                current_animation = self.player_run_right
    

        #animation
        current_animation_tick = pygame.time.get_ticks()
        if current_animation_tick - self.last_animation_tick > self.animation_cooldown: #trigger animation on delay
            self.animation_index += 1
            self.last_animation_tick = current_animation_tick

            if self.animation_index >= len(current_animation): #prevent out of bound exception
                self.animation_index = 0

            if self.last_animation_play != current_animation: #start on first animation sequence
                self.animation_index = 0
                self.last_animation_play = current_animation

            self.image = current_animation[self.animation_index]  #animation sequence to use

        #gravity
        self.velocity += 1 #gravity fall
        if self.velocity > 10: #peak velocity
            self.velocity = 10
        delta_y += self.velocity
        
        #world collision
        self.rect.x += delta_x #x-direction collision
        if pygame.sprite.spritecollide(self, world.block_group, False):
            self.rect.x -= delta_x #don't apply movement on wall collision
        
        self.rect.y += delta_y #y-direction collision
        if pygame.sprite.spritecollide(self, world.block_group, False):
 
            if self.velocity >= 0: #bottom collision (grounded)
                self.hasJumped = False

            self.rect.y -= delta_y #don't apply movement on ground collision     
            self.velocity = 0    