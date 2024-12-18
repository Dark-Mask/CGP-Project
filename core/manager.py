class GameManager:
    def __init__(self):
        self.time = 0
        self.collected = 0

    def track_time(self, time):
        self.time += time

    def track_collection(self, count):
        self.collected += count