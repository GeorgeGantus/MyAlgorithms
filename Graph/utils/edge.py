class Edge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight

    def __repr__(self):
        return f"Weight: {self.weight}, Target: {self.target}"

