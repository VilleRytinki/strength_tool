class Session():

    def __init__(self, date, name, exercises, duration):
        self.date = date
        self.name = name
        self.exercises = exercises
        self.duration = duration

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

    def get_exercises(self):
        for exercise in self.exercises:
            print(exercise.get_exercise_information())
        # return self.exercises

    def set_duration(self, duration):
        self.duration = duration

    def get_duration(self):
        return self.duration

    def get_session_information(self):
        print('date', self.date, 'SessionTitle:', self.name, 'duration:',
              self.duration)
        self.get_exercises()
