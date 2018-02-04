class Position:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{}(x={}, y={})".format(self.__class__.__name__, self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, __class__):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))
