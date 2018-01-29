from . import Entity

class World:
    def __init__(self):
        self.entities = {}
        self.last_id = 0
        self.processors = []
        self.name_map = {}

    def create_entity(self, **kwargs):
        entity = Entity(self)
        if 'name' in kwargs:
            entity.name = kwargs['name']
        self.last_id += 1
        self.entities[self.last_id] = entity
        return self.entities[self.last_id]

    def add_processor(self, processor):
        processor.world = self
        self.processors.append(processor)

    def get(self, **kwargs):
        if 'name' in kwargs:
            name = kwargs['name']
            if name in self.name_map:
                return self.name_map[name]
        return None

    def _set_name(self, entity, name):
        if entity.name in self.name_map:
            del self.name_map[name]
        self.name_map[name] = entity

