import sys
import pygame
from configuration import *
from weapons import *
from sprites import *

class Spritesheet:
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path).convert()
    
    def get_image(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.spritesheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init() 
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.lava_spritesheet = Spritesheet('assets/images/lava.png')
        self.player_spritesheet = Spritesheet('assets/images/player.png')
        self.fire_enemy_spritesheet = Spritesheet('assets/images/fireEvil.png')
        self.ice_enemy_spritesheet = Spritesheet('assets/images/iceEvil.png')
        self.poison_enemy_spritesheet = Spritesheet('assets/images/poisonEvil.png')
        self.fire_bullet_spritesheet = Spritesheet('assets/images/fireball.png')
        self.ice_bullet_spritesheet = Spritesheet('assets/images/ice.png')
        self.poison_bullet_spritesheet = Spritesheet('assets/images/poison.png')
        self.bullet_spritesheet = Spritesheet('assets/images/heroBall.png')
        self.weapon_spritesheet = Spritesheet('assets/images/heroBall.png')
        self.floor_spritesheet = Spritesheet('assets/images/floor.png')
        self.block_spritesheet = Spritesheet('assets/images/block.png')
        self.healthpack_spritesheet = Spritesheet('assets/images/health.png')
        self.running = True
        self.enemy_collided = False
        self.block_collided = False

    def createTileMap(self):
        player_spawned = False
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Floor(self, j, i)
                if column == 'B':
                    Block(self, j, i)
                elif column == 'P' and not player_spawned:
                    self.player = Player(self, j, i)
                    player_spawned = True
                elif column == 'E':
                    FireEnemy(self, j, i)
                elif column == 'I':
                    IceEnemy(self, j, i)
                elif column == 'O':
                    PoisonEnemy(self, j, i)
                elif column == 'L':
                    Lava(self, j, i)
                elif column == 'W':
                    Weapon(self, j, i)
                elif column == 'H':
                    HealthPack(self, j, i)
                elif column == 'N':
                    Void(self, j, i)

    def center_camera_on_player(self):
        for sprite in self.all_sprites:
            sprite.rect.x -= self.player.rect.x - WIN_WIDTH // 2
            sprite.rect.y -= self.player.rect.y - WIN_HEIGHT // 2
        self.player.rect.x = WIN_WIDTH // 2
        self.player.rect.y = WIN_HEIGHT // 2

    def create(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.lava = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.mainPlayer = pygame.sprite.LayeredUpdates()
        self.weapons = pygame.sprite.LayeredUpdates()
        self.bullets = pygame.sprite.LayeredUpdates()
        self.healthbar = pygame.sprite.LayeredUpdates()
        self.healthpacks = pygame.sprite.LayeredUpdates()
        self.createTileMap()
        self.center_camera_on_player()

    def update(self):
        self.all_sprites.update()
        self.check_victory()

    def check_victory(self):
        if not self.enemies:
            self.victory_menu()

    def game_over_menu(self):
        font = pygame.font.Font(None, 74)
        text = font.render('Гра Закінчена', True, RED)
        self.screen.blit(text, (WIN_WIDTH // 2 - text.get_width() // 2, WIN_HEIGHT // 2 - text.get_height() // 2 - 50))
        
        font = pygame.font.Font(None, 30)
        restart_button = pygame.Rect(WIN_WIDTH // 2 - 100, WIN_HEIGHT // 2 + 50, 200, 50)
        exit_button = pygame.Rect(WIN_WIDTH // 2 - 100, WIN_HEIGHT // 2 + 150, 200, 50)
        pygame.draw.rect(self.screen, GREEN, restart_button)
        pygame.draw.rect(self.screen, GREEN, exit_button)
        
        restart_button_text = font.render('Перезапустити(R)', True, BLACK)
        exit_button_text = font.render('Вийти(Q)', True, BLACK)
        self.screen.blit(restart_button_text, (restart_button.x + (restart_button.width - restart_button_text.get_width()) // 2, restart_button.y + (restart_button.height - restart_button_text.get_height()) // 2))
        self.screen.blit(exit_button_text, (exit_button.x + (exit_button.width - exit_button_text.get_width()) // 2, exit_button.y + (exit_button.height - exit_button_text.get_height()) // 2))
        
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.create()
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if restart_button.collidepoint(event.pos):
                            self.create()
                            waiting = False
                        elif exit_button.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

    def victory_menu(self):
        font = pygame.font.Font(None, 74)
        text = font.render('Ви Перемогли!', True, GREEN)
        self.screen.blit(text, (WIN_WIDTH // 2 - text.get_width() // 2, WIN_HEIGHT // 2 - text.get_height() // 2 - 50))
        
        font = pygame.font.Font(None, 30)
        restart_button = pygame.Rect(WIN_WIDTH // 2 - 100, WIN_HEIGHT // 2 + 50, 200, 50)
        exit_button = pygame.Rect(WIN_WIDTH // 2 - 100, WIN_HEIGHT // 2 + 150, 200, 50)
        pygame.draw.rect(self.screen, GREEN, restart_button)
        pygame.draw.rect(self.screen, GREEN, exit_button)
        
        restart_button_text = font.render('Перезапустити(R)', True, BLACK)
        exit_button_text = font.render('Вийти(Q)', True, BLACK)
        self.screen.blit(restart_button_text, (restart_button.x + (restart_button.width - restart_button_text.get_width()) // 2, restart_button.y + (restart_button.height - restart_button_text.get_height()) // 2))
        self.screen.blit(exit_button_text, (exit_button.x + (exit_button.width - exit_button_text.get_width()) // 2, exit_button.y + (exit_button.height - exit_button_text.get_height()) // 2))
        
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.create()
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if restart_button.collidepoint(event.pos):
                            self.create()
                            waiting = False
                        elif exit_button.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def camera(self):
        if not self.enemy_collided and not self.block_collided:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                for sprite in self.all_sprites:
                    sprite.rect.x += PLAYER_STEPS
            elif pressed[pygame.K_RIGHT]:
                for sprite in self.all_sprites:
                    sprite.rect.x -= PLAYER_STEPS
            elif pressed[pygame.K_UP]:
                for sprite in self.all_sprites:
                    sprite.rect.y += PLAYER_STEPS
            elif pressed[pygame.K_DOWN]:
                for sprite in self.all_sprites:
                    sprite.rect.y -= PLAYER_STEPS

    def main(self):
        while self.running:
            self.events()
            self.camera()
            self.update()
            self.draw()

game = Game()
game.create()

while game.running:
    game.main()

pygame.quit()
sys.exit()
