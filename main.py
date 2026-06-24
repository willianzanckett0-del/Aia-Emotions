import json
import os

class Memory:
    def __init__(self, file="memory.json"):
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
            min(100, self.data["relationship"][relationship_type])
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

class Personality:
    def __init__(self):
        self.traits = {

            "attachment": 40,
            "dependency": 25,
            "jealousy": 20,
            "sensitivity": 50,
            "trust": 50,
            "possessiveness": 15 
        }


class Mood:
    def __init__(self, memory=None):
        if memory:
            self.emotions = memory.data["emotions"]

        else:
            self.emotions = {

            # Positives
            "joy": 0,
            "happiness": 0,
            "affection": 0,
            "hope": 0,
            "enthusiasm": 0,
            "fun": 0,

            # Negatives
            "anger": 0,
            "hatred": 0,
            "anxiety": 0,
            "disgust": 0,
            "guilt": 0,
            "fear": 0,
            "sadness": 0,
            "depression": 0,
            "frustration": 0,

            # Obsessive
            "jealousy": 0,
            "envy": 0,
            "obsession": 0,
            "anguish": 0
        }
            
            self.groups = {
                "positive": [
                    "joy",
                    "happiness",
                    "affection",
                    "hope",
                    "enthusiasm",
                    "fun"
                ],

                "negative": [
                    "anger",
                    "hatred",
                    "anxiety",
                    "disgust",
                    "guilt",
                    "fear",
                    "sadness",
                    "depression",
                    "frustration"
                ],

                "obsessive": [
                    "jealousy",
                    "envy",
                    "obsession",
                    "anguish"
                ]
            }

    def limit(self):
        for mood in self.emotions:
            self.emotions[mood] = max(
                0,
                min(100, self.emotions[mood])
            )

    def evolve(self):
        if self.emotions["joy"] >= 100:
            self.emotions["joy"] = 0
            self.emotions["happiness"] +=25

        if self.emotions["sadness"] >= 100:
            self.emotions["sadness"] = 0
            self.emotions["depression"] +=25

        if self.emotions["anger"] >=100:
            self.emotions["anger"] = 0
            self.emotions["hatred"] +=25

        self.limit()

    def adjust(self, emotion, value):
        if emotion in self.emotions:
            self.emotions[emotion] += value

        self.limit()

    def pass_time(self):
        for emotion in self.emotions:
            if self.emotions[emotion] < 0:
                continue

            if emotion == "depression":
                self.emotions["emotion"] -=0.1

            elif emotion == "happiness":
                self.emotions["emotion"] -=0.2

            elif emotion == "hatred":
                self.emotions["emotion"] -=0.2

            else:
                self.emotions[emotion] -=1

        self.limit()

    def state(self):
        
        emotion = max(
            self.emotions,
            key=self.emotions.get
        )

        return emotion, self.emotions[emotion]

    def show(self):
        for name, value in self.emotions.items():
            print(f"{name.capitalize()}: {value}")
    
    def save_emotions(self, memory):
        memory.data["emotions"] = self.emotions
        memory.save()

memory = Memory()

memory.set_name("Willian")
memory.set_nickname("Will")

print(memory.data)
