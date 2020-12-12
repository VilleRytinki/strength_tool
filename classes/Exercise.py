class Exercise:

    def __init__(self, id, name, weight, work_sets, repetitions):
        self.id = id
        self.name = name
        self.weight = weight
        self.work_sets = work_sets
        self.repetitions = repetitions
        self.volume
        self.tonnage
        self.intensity
        self.session_date

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_sets(self):
        return self.work_sets

    def set_sets(self, sets):
        self.work_sets = sets

    def get_repetitions(self):
        return self.repetitions

    def set_repetitions(self, repetitions):
        self.repetitions = repetitions

    def get_info(self):
        return {'Exercise': self.name, 'weight': self.weight, 'sets': self.work_sets, 'repetitions': self.repetitions}

    def get_volume(self):
        sets = self.get_sets()
        repetitions = self.get_repetitions()

        return sets * repetitions

    def get_tonnage(self):
        sets = self.get_sets()
        repetitions = self.get_repetitions()
        weight = self.get_weight()

        return weight * repetitions * sets
