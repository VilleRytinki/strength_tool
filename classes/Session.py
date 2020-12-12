from classes.Exercise import Exercise


class Session:

    def __init__(self, date, name, exercises, duration):
        self.date = date
        self.name = name
        self.exercises = []
        self.duration = duration
        self.total_volume
        self.total_tonnage

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_exercises(self, exercises):
        self.exercises = exercises

    def print_exercises(self):
        for exercise in self.exercises:

            exercise_name = exercise.get_name()
            exercise_weight = exercise.get_weight()
            exercise_work_sets = exercise.get_sets()
            exercise_repetitions = exercise.get_repetitions()

            print('Exercise:', exercise_name, 'Weight:', exercise_weight, 'Work Sets:', exercise_work_sets,
                  'Repetitions:', exercise_repetitions)

    def set_duration(self, duration):
        self.duration = duration

    def get_duration(self):
        return self.duration

    def get_session_information(self):
        print('Session:', self.name, 'date', self.date, 'duration:', self.duration)
        self.print_exercises()

    def calculate_volume_for_all(self):
        print('Volume of all exercises in {} titled {}.'.format(self.date, self.name))
        for exercise in self.exercises:
            volume = exercise.get_volume()
            name = exercise.get_name()
            print('Volume for exercise {} was {}.'.format(name, volume))

    def calculate_volume_for_exercise(self, exercise_name):
        volume = 0.0

        for exercise in self.exercises:
            if exercise.get_name() == exercise_name:
                exercise_volume = exercise.get_volume()
                name = exercise.get_name()
                print('Volume for exercise {} in {} was {}'.format(name, self.date, exercise_volume))
                volume += exercise_volume
        print('Total volume for exercise {} was {}'.format(name, volume))

    def calculate_tonnage_for_all(self):
        print('Tonnage of all exercises in {} titled {}.'.format(self.date, self.name))
        for exercise in self.exercises:
            tonnage = exercise.get_tonnage()
            name = exercise.get_name()
            print('Tonnage for exercise {} was {}'.format(name, tonnage))

    def calculate_tonnage_for_exercise(self, exercise_name):
        tonnage = 0.0

        for exercise in self.exercises:
            if exercise.get_name() == exercise_name:
                exercise_tonnage = exercise.get_tonnage()
                name = exercise.get_name()
                print('Tonnage for exercise {} in {} was {}'.format(name, self.date, exercise_tonnage))
                tonnage += exercise_tonnage
        print('Total tonnage for exercise {} was {}'.format(name, tonnage))
