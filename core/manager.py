class GameManager:
    def __init__(self):
        self.time = 0
        self.collected = 0
        self.game_status = 'winner'

    def track_time(self, time):
        self.time += time

    def track_collection(self, count):
        self.collected += count

    def set_gameover(self):
        self.game_status = 'gameover'

    def get_status(self):
        return self.game_status