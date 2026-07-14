class Personality:
    def __init__(self):
        self.traits = {

            "attachment": 400,
            "dependency": 250,
            "jealousy": 200,
            "sensitivity": 500,
            "trust": 500,
            "possessiveness": 150 
        }

    def modify_emotion(self, emotion, value):
        final = value
        
        final *= 1 + (self.traits["sensitivity"] / 1000)

        if emotion in [
            "joy",
            "happiness",
            "affection",
            "hope",
            "enthusiasm",
            "fun"
        ]:
            final *= 1 + (self.traits["attachment"] / 1000)

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
            final *=1 + (self.traits["dependency"] / 1000)

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
                self.traits["trust"] / 1000
            )

            final *= (1 - reduction)
        
        return max(1, round(final))