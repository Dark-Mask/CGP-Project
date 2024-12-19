import os, json, pygame
import components.player as player
import core.manager as manager
import core.status as status
from world import *
from pygame.locals import *

class Game():

    def __init__(self):
        
        self.width = 1200
        self.height = 700
        self.tile_size = 30

        self.maps = {
            "forest" : map.Forest,
            "snow" : map.Snow,
            "cemetery" : map.Cemetery
        }
        self.levels = []
        self.game_manager = manager.GameManager()
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
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Jolly Jumpers - Game')
        clock = pygame.time.Clock()
        
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
                        self.game_manager.shutdown(True)
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

                game_world.draw(screen)
                game_player.draw(screen)
                game_player.player_border(screen)
                game_status.draw(screen)
                # game_world.draw_grid(screen)
                pygame.display.update()

                #check condition and update score
                if not game_status.has_heatlh():
                    self.game_manager.set_gameover(True)
                    run = False
                elif game_status.has_completed():
                    pygame.time.wait(1800)
                    run = False
                    
                clock.tick(fps)

            #level score
            self.game_manager.track_collection(game_status.collected)
            self.game_manager.track_time(game_status.time)

            #break level game loop
            if self.game_manager.is_gameover() or self.game_manager.is_shutdown():
                break

        #close window
        pygame.display.quit()
        return self.game_manager
