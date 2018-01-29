class Grid:
    def __init__(self, width, height, default_value=None):
        self.width = width
        self.height = height
        self.default_value = default_value
        self.values = []

    def __getitem__(self, key):
        if not self.within_bounds(key):
            return
        x, y = key
        if len(self.values) <= y or len(self.values[y]) <= x:
            return self.default_value
        return self.values[y][x]

    def __setitem__(self, key, value):
        if not self.within_bounds(key):
            return
        x, y = key
        while len(self.values) <= y:
            self.values.append([])
        while len(self.values[y]) <= x:
            self.values[y].append(self.default_value)
        self.values[y][x] = value

    def within_bounds(self, key):
        return 0 <= key[0] < self.width and 0 <= key[1] < self.height
