import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, player_group, player_mode, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 100))
        self.image.fill("white")

        self.rect = self.image.get_rect()

        self.player_group = player_group
        self.player_mode = player_mode
        self.screen = screen

        self.player_group.add(self)

        self.current_state = "init"

        self.speed = 250
        self.speed_y = 0

        self.keys = {}
        self.spawn_pos = 0

        match player_mode:
            case 1:
                self.keys.update(up=pygame.K_w, down=pygame.K_s)
                self.spawn_pos = (30, self.screen.get_size()[1]//2 - 50)
            case 2:
                self.keys.update(up=pygame.K_UP, down=pygame.K_DOWN)
                self.spawn_pos = (self.screen.get_size()[0] - 45, self.screen.get_size()[1]//2 - 50)
        
        self.rect.center = self.spawn_pos
    

    def state_machine(self, delta):
        match self.current_state:
            case "init":
                self.rect.center = self.spawn_pos
                self.current_state = "move"
            case "move":
                self.move(delta)


    def move(self, delta):
        self.rect.clamp_ip((0, 0, self.screen.get_size()[0], self.screen.get_size()[1]))

        self.speed_y = 0

        if pygame.key.get_pressed()[self.keys.get("up")]:
            self.speed_y = -self.speed
        elif pygame.key.get_pressed()[self.keys.get("down")]:
            self.speed_y = self.speed

        self.rect.centery += self.speed_y * delta


    def update(self, *args, **kwargs):
        self.state_machine(kwargs.get("delta"))

        return super().update(*args, **kwargs)