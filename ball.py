import pygame

from random import choice

class Ball(pygame.sprite.Sprite):
    def __init__(self, ball_group, player_group, screen, marker):
        pygame.sprite.Sprite.__init__(self)

        self.ball_group = ball_group
        self.player_group = player_group
        self.screen = screen
        self.marker = marker

        self.ball_group.add(self)

        self.current_state = "init"

        self.speed = 250
        self.speed_x, self.speed_y = self.speed, self.speed

        self.radius = 6.7
        self.spawn_pos = (self.screen.get_size()[0] / 2, self.screen.get_size()[1] / 2)

        self.image = pygame.Surface((self.radius * 2, self.radius * 2),
                                    pygame.SRCALPHA)

        pygame.draw.circle(self.image, "white", (self.radius, self.radius), self.radius)

        self.rect = self.image.get_rect()
        self.rect.center = self.spawn_pos
    

    def state_machine(self, delta):
        match self.current_state:
            case "init":
                self.rect.center = self.spawn_pos

                self.speed_x = self.speed * 0.7071 * choice([-1, 1])
                self.speed_y = self.speed * 0.7071 * choice([-1, 1])

                self.current_state = "move"
            
            case "move":
                self.check_collision()
                self.check_walls()
                self.move(delta)


    def check_collision(self):
        for player in self.player_group:
            if self.rect.colliderect(player.rect):
                relative = (
                    self.rect.centery - player.rect.centery
                ) / (player.rect.height / 2)

                self.speed_y = relative * self.speed
                self.speed_x *= -1

                if abs(self.speed_y) < 50:
                    self.speed_y = 50 * (1 if self.speed_y >= 0 else -1)

                self.speed_x *= 1.05
                self.speed_y *= 1.05


    def reset_game(self):
        self.current_state = "init"

        for player in range(len(self.player_group.sprites())):
            self.player_group.sprites()[player].current_state = "init"
        
        pygame.time.wait(500)


    def update_points(self, scored):
        match scored:
            case "player_one":
                self.marker.player_one_score += 1
            case "player_two":
                self.marker.player_two_score += 1
    

    def check_walls(self):
        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_size()[1]:
            self.speed_y *= -1
        
        if self.rect.left <= 0:
            self.update_points("player_two")
            self.reset_game()
        
        elif self.rect.right >= self.screen.get_size()[0]:
            self.update_points("player_one")
            self.reset_game()
        

    def move(self, delta):
        self.rect.centerx += self.speed_x * delta
        self.rect.centery += self.speed_y * delta
    
    
    def update(self, *args, **kwargs):
        self.state_machine(kwargs.get("delta"))

        return super().update(*args, **kwargs)
