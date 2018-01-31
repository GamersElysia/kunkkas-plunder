class Processor:

    def __init__(self):
        self.world = None

    def update(self):
        # This method should be overriden by child classes to add processing
        # logic to a world.
        pass

    def get_data(self, key=None):
        if key is None:
            return self.world.data
        return self.world.data[key]
