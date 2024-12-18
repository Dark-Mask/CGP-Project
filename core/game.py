import os
import json
import pygame
import components.player as player
from core import *
from world import *
from pygame.locals import *

class Game():

    def __init__(self):
        
        self.maps = {
            "forest" : map.Forest,
            "snow" : map.Snow,
            "cemetery" : map.Cemetery
        }
        self.levels = []
        self.game_manager = manager.GameManager()
        self.screen = pygame.display.set_mode((1200, 700))
        self.clock = pygame.time.Clock()
        self._load_levels()


    def _load_levels(self):
        level_dir = 'levels'
        files = os.listdir(level_dir)

        for level in files:
            level_path = f'{level_dir}/{level}'
            if(os.path.isfile(level_path)):
                #read level data and store as python dictionary
                with open(level_path, 'r') as data:
                    json_data = json.loads(data.read())
                    self.levels.append(json_data)


    def start(self, fps=60):
        result = ''

        for level in self.levels:
            world_map = self.maps[level['world']]
            word_data = level['world_data']
            game_world = world_map(word_data)

            game_status = status.GameStatus(game_world)
            game_player = player.Player(100, game_world.height - 130, 45, 60)

            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
            
                #enemy collision
                if pygame.sprite.spritecollide(game_player, game_world.enemy_group, True):
                    game_status.damage(70)

                #bullet hit
                if pygame.sprite.spritecollide(game_player, game_world.bullet_group, True):
                    game_status.damage(50)

                #item collect
                if pygame.sprite.spritecollide(game_player, game_world.collect_group, True):
                    game_status.item_collected()


                game_world.update()
                game_player.update(game_world)
                game_status.update()

                game_world.draw(self.screen)
                game_player.draw(self.screen)
                game_player.player_border(self.screen)
                game_status.draw(self.screen)
                # game_world.draw_grid(screen)

                #draw complete level
                if game_status.is_winner():
                    game_status.next_level(self.screen)

                pygame.display.update()

                #check condition
                if game_status.is_gameover():
                    result = 'gameover'
                    run = False
                elif game_status.is_winner():
                    result = 'winner'
                    pygame.time.wait(2000)
                    run = False
                    
                self.clock.tick(fps)

            if game_status.is_gameover():
                break

        #close window
        pygame.display.quit()
        return result
