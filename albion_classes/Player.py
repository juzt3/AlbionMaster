from collections import deque


class Player:

    def __init__(self):
        self.char_id = None
        self.mark_id = None
        self.name = None
        self.cluster = None
        self.pos = None
        self.prev_pos = deque(maxlen=10)
        self.target_pos = None
        self.speed = None
        self.angle = None
        self.current_health = None
        self.max_health = None
        self.current_energy = None
        self.max_energy = None
        self.current_silver = None
        self.faction = 0
        self.death_counter = 0

    def init(self, char_id, markId, name, cluster, pos, current_health, max_health, current_energy, max_energy, faction):
        self.char_id = char_id
        self.mark_id = markId
        self.name = str(name)
        self.cluster = str(cluster)
        self.pos = tuple(pos)
        self.current_health = int(current_health)
        self.max_health = int(max_health)
        self.current_energy = int(current_energy)
        self.max_energy = int(max_energy)
        self.faction = int(faction)

    def set_pos(self, pos: tuple):
        self.pos = pos
        self.prev_pos.append(pos)

    def get_prev_positions(self):
        return list(self.prev_pos)

    def isAllyRoyal(self, faction):
        if faction == 0 or (faction == self.faction and faction != 255) or (self.faction == 0 and faction != 255):
            return True
        return False
