class AtomClass:
    def __init__(self, Velocity, Element = 'C', Mass = 12.0):
        self.Velocity = Velocity
        self.Element = Element
        self.Mass = Mass
    def Momentum(self):
        return self.Velocity * self.Mass
