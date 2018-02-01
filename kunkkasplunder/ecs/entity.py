class Entity:

    def __init__(self, world):
        self._name = None
        self.tags = []
        self._world = world
        self.components = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._world._set_name(self, value)
        self._name = value

    @property
    def world(self):
        return self._world

    def add(self, component):
        t = type(component)
        if t not in self.components:
            self.components[t] = []
        self.components[t].append(component)

    def has(self, component_type):
        return component_type in self.components

    def get(self, component_type):
        if component_type in self.components:
            return self.components[component_type][0]
        else:
            return None
