class Condition:
    def __init__(self, condition: dict):
        self.waterflow = condition["waterflow"]
        self.temperature = condition["temperature"]
        self.pressure = condition["pressure"]
        self.waterfeed = condition["waterfeed"]
