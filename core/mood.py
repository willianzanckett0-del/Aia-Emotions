class Mood:
    def __init__(self, memory=None, personality=None):
        self.personality = personality
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
        if emotion not in self.emotions:
            return
        
        if self.personality:
            value = self.personality.modify_emotion(
                emotion,
                value
            )

        self.emotions[emotion] += value

        self.limit()
        self.evolve()

    def pass_time(self):
        for emotion in self.emotions:
            if self.emotions[emotion] <= 0:
                continue

            if emotion == "depression":
                self.emotions[emotion] -=0.1

            elif emotion == "happiness":
                self.emotions[emotion] -=0.2

            elif emotion == "hatred":
                self.emotions[emotion] -=0.2

            else:
                self.emotions[emotion] -=1

        self.limit()

    def state(self):
        
        emotion = max(
            self.emotions,
            key=self.emotions.get
        )

        return emotion, self.emotions[emotion]
    
    def save_emotions(self, memory):
        memory.data["emotions"] = self.emotions
        memory.save()
