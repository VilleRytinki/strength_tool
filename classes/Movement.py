
class Movement:

    def __init__(self, name, weight, sets, repetitions):
        self.name = name
        self.weight = weight
        self.sets = sets
        self.repetitions = repetitions

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_sets(self):
        return self.sets

    def set_sets(self, sets):
        self.sets = sets

    def get_repetitions(self):
        return self.repetitions

    def set_repetitions(self, repetitions):
        self.repetitions = repetitions

    def print_movement_information(self):
        return {'name': self.name, 'weight': self.weight, 'sets': self.sets, 'repetitions': self.repetitions}
