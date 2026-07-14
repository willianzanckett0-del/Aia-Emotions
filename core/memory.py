import json
import os

class Memory:
    def __init__(self, file="saves/memory.json"):
        self.file = file
        self.data = self.load()

    def default_structure(self):
        return {
            "user": {
                "name": "",
                "nickname": ""
            },

            "relationship": {
                "affinity": 0,
                "trust": 0,
                "care": 0
            },

            "emotions": {
                "joy": 0,
                "happiness": 0,
                "affection": 0,
                "hope": 0,
                "enthusiasm": 0,
                "fun": 0,

                "anger": 0,
                "hatred": 0,
                "anxiety": 0,
                "disgust": 0,
                "guilt": 0,
                "fear": 0,
                "sadness": 0,
                "depression": 0,
                "frustration": 0,

                "jealousy": 0,
                "envy": 0,
                "obsession": 0,
                "anguish": 0
            },

            "history": [],
            "preferences": {},
            "events": {}
        }

    def load(self):
        if not os.path.exists(self.file):
            data = self.default_structure()

            with open(self.file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            return data
        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    # User
    def set_name(self, name):
        self.data["user"]["name"] = name
        self.save()

    def set_nickname(self, nickname):
        self.data["user"]["nickname"] = nickname
        self.save()
    

    def save(self):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)
            
    # Relationship
    def change_relationship(self, relationship_type, value):
        self.data["relationship"][relationship_type] += value
        self.data["relationship"][relationship_type] = max(
            0,
            min(1000, self.data["relationship"][relationship_type])
        )
        self.save()

    # History
    def add_history(self, event):
        self.data["history"].append(event)
        self.save()

    # Event
    def count_event(self, name):
        if name not in self.data["events"]:
            self.data["events"][name] = 0
        self.data["events"][name] += 1
        self.save()

    def get_event(self, name):
        return self.data["events"].get(name, 0)
