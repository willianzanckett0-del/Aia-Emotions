class DialogueEngine:

    def __init__(self, mood, memory):
        self.mood = mood
        self.memory = memory

    def execute(self, option):

        if "emotion" in option:

            for emotion, value in option["emotion"].items():
                self.mood.adjust(emotion, value)

        if "relationship" in option:

            for rel, value in option["relationship"].items():
                self.memory.change_relationship(rel, value)

        self.mood.save_emotions(self.memory)
        return option["response"], option["next"]



