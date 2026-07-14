class Conversation:

    def __init__(self):
        self.file = "neutral"
        self.section = "questions"

    def change_file(self, new_file):
        self.file = new_file

    def get_file(self):
        return self.file

    def change_section(self, new_section):
        self.section = new_section

    def get_section(self):
        return self.section