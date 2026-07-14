import json
import os
import random


class Dialog:

    def __init__(self):

        self.folder = "data/dialogs"
    
    def get_choices(self, emotion, section):
        
        path = os.path.join(
            self.folder,
            f"{emotion}.json"
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            dialogs = json.load(file)
            
        return dialogs[section]
    
    def get_start(self, emotion):

        path = os.path.join(
            self.folder,
            f"{emotion}.json"
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:
            
            dialogs = json.load(file)

        return random.choice(dialogs["start"])


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

        path = os.path.join(
            self.folder,
            f"{emotion}.json"
        )

        with open(path, "r", encoding="utf-8") as file:
            dialogs = json.load(file)

        return random.choice(dialogs)