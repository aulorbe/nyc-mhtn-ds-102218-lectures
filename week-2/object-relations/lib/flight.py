class Flight:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("Getting name")
        return self._name

    def set_name(self, name):
        print("Setting name")
        self._name = _name

    name = property (get_name, set_name)
