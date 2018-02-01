class Position:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{}(x={}, y={})".format(self.__class__.__name__, self.x, self.y)

    def __eq__(self, comparator):
        if self.x == comparator.x and self.y == comparator.y:
            return True
        else:
            return False