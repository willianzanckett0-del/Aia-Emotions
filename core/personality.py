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

    def modify_emotion(self, emotion, value):
        final = value
        
        final *= 1 + (self.traits["sensitivity"] / 100)

        if emotion in [
            "joy",
            "happiness",
            "affection",
            "hope",
            "enthusiasm",
            "fun"
        ]:
            final *= 1 + (self.traits["attachment"] / 100)

        elif emotion in [
            "jealousy",
            "envy",
            "obsession",
            "anger",
            "hatred"
        ]:
            final *= 1 + (self.traits["jealousy"] / 100)

        elif emotion in [
            "sadness",
            "depression",
            "anxiety",
            "anguish"
        ]:
            final *=1 + (self.traits["dependency"] / 100)

        negative_trust = [
            "anger",
            "hatred",
            "fear",
            "anxiety",
            "sadness",
            "depression",
            "anguish"
        ]

        if emotion in negative_trust:

            reduction = (
                self.traits["trust"] / 100
            )

            final *= (1 - reduction)
        
        return max(1, round(final))