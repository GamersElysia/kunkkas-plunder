import itertools

from .position import Position


class Grid:

    def __init__(self, width, height, default_value=None):
        self.width = width
        self.height = height
        self.default_value = default_value
        self.values = []

    def __getitem__(self, key):
        if isinstance(key, Position):
            x, y = key.x, key.y
        else:
            x, y = key
        if not self._within_bounds(x, y):
            return
        if len(self.values) <= y or len(self.values[y]) <= x:
            return self.default_value
        return self.values[y][x]

    def __setitem__(self, key, value):
        if isinstance(key, Position):
            x, y = key.x, key.y
        else:
            x, y = key
        if not self._within_bounds(x, y):
            return
        while len(self.values) <= y:
            self.values.append([])
        while len(self.values[y]) <= x:
            self.values[y].append(self.default_value)
        self.values[y][x] = value

    def __iter__(self):
        """Iterate over all (x, y) tuples making up the coordinates of the Grid.

        The x coordinate is increased first so the order of iteration is:
        (0, 0) (1, 0) ... (0, 1) (1, 1) ...
        """
        return map(reversed, itertools.product(
            range(self.height), range(self.width)))

    def _within_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
