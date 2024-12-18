class GameManager:
    def __init__(self):
        self._time = 0
        self._collected = 0
        self._gameover = False

    def track_time(self, time):
        self._time += time

    def track_collection(self, count):
        self._collected += count

    def set_gameover(self, status):
        self._gameover = status

    def is_gameover(self):
        return self._gameover
    
    def final_time(self):
        return self._time

    def final_collection(self):
        return self._collected