class Trainee:

    def __init__(self, name, height, weight):
        self.id
        self.name = name
        self.height = height
        self.weight = weight
        self.training_log
        self.sq_pr
        self.dl_pr
        self.bb_pr
        self.p_pr


    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def add_to_log(self, session):
        self.training_log.append(session)

    def get_log(self):
        return self.training_log

    def print_log(self):
        for session in self.training_log:
            session.get_session_information()
