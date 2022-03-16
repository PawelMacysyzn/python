import pygame
import sys


def collid_sprite_with_rect(sprite_1, sprite_2):
    if sprite_1.rect.colliderect(sprite_2.rect):
        sprite_1.image.fill('red')
    else:
        sprite_1.image.fill('green')


def collid_sprite_with_mask(player_mask, obstacle_mask, obsticle_x, obsticle_y, player_x, player_y, player_surface):
    offset_x = obsticle_x - player_x
    offset_y = obsticle_y - player_y
    if player_mask.overlap(obstacle_mask, (offset_x, offset_y)):
        player_surface.fill('red')
    else:
        player_surface.fill('green')


pygame.init()
# game window application
screen = pygame.display.set_mode((800, 800))
screen_rect = screen.get_rect(center=(screen.get_width(), screen.get_height()))
# width and height of screen
scree_rect_w_h = screen_rect[0], screen_rect[1]

# player
player_sprite = pygame.sprite.Sprite()
player_sprite.image = pygame.Surface((30, 30))
# mask
player_mask = pygame.mask.from_surface(player_sprite.image)

# obstacle
obstacle_sprite = pygame.sprite.Sprite()
obstacle_sprite.image = pygame.image.load(
    'detection_collision/beta.png').convert_alpha()
obstacle_pos = (100, 100)
obstacle_sprite.rect = obstacle_sprite.image.get_rect(topleft=obstacle_pos)
# obstacle_sprite.rect = obstacle_sprite.image.get_rect(center=(scree_rect_w_h))
# mask
obstacle_mask = pygame.mask.from_surface(obstacle_sprite.image)
# clock
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # mouse co-ordinates
    destination = pygame.mouse.get_pos()
    player_sprite.rect = player_sprite.image.get_rect(center=destination)
    screen.fill('white')  # cleaning screen
    # draw obstacle_sprite
    screen.blit(obstacle_sprite.image, obstacle_sprite.rect)
    # draw player
    screen.blit(player_sprite.image, player_sprite.rect)

    # collision with obstacle rect
    # # collid_sprite_with_rect(player_sprite, obstacle_sprite)

    # collision with obstacle mask
    collid_sprite_with_mask(player_mask, obstacle_mask,
                            obstacle_sprite.rect[0], obstacle_sprite.rect[1], player_sprite.rect.left, player_sprite.rect.top, player_sprite.image)

    pygame.display.update()
    clock.tick(60)
