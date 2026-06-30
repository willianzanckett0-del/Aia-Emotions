import json
import random


class Dialog:

    def __init__(self):

        with open(
            "data/dialogs.json",
            "r",
            encoding="utf-8"
        ) as file:

            self.dialogs = json.load(file)
    
    def get_choices(self, state):
        return self.dialogs[state]


    def get_dialog(self, emotion):

        if emotion in [
            "joy",
            "happiness",
            "hope",
            "enthusiasm"
        ]:
            emotion = "affection"


        elif emotion in [
            "jealousy",
            "envy"
        ]:
            emotion = "jealousy"


        elif emotion in [
            "obsession",
            "anguish"
        ]:
            emotion = "obsession"


        else:
            emotion = "neutral"


        return random.choice(
            self.dialogs[emotion]
        )