import pygame, random
pygame.init()


# Set display settings
screen_width = 700
screen_height = 700
screen_color = (200, 200, 200)

display = pygame.display.set_mode((screen_width, screen_height))


# Player object - Represents the user sprite
class Player(object):
    def __init__(self, x_pos, y_pos, width, height, velocity):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.velocity = velocity

    def draw(self):
        pygame.draw.rect(display, (255, 0, 0), (self.x_pos, self.y_pos, self.width, self.height))


# Create player
player_width = 40
player_height = 30
player_velocity = 3

player = Player(screen_width * 0.5 - (player_width / 2),
                screen_height - player_height - player_velocity,
                player_width, player_height, player_velocity)


def redraw_game_window():
    display.fill(screen_color)
    pygame.draw.rect(display, (255, 255, 255), (0, 0, screen_width, screen_height * 0.6))
    player.draw()
    pygame.display.update()


running = True
while running:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x_pos > player.velocity:
        player.x_pos -= player.velocity

    if keys[pygame.K_RIGHT] and player.x_pos < screen_height - player.width - player.velocity:
        player.x_pos += player.velocity

    redraw_game_window()

pygame.quit()
