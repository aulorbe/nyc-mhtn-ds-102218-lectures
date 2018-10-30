class Airline():
    def __init__(self, name, year):
        self._name = name
        self._year = year

    def get_name(self):
        print("Getting name")
        return self._name

    def set_name(self, name):
        print("Setting name")
        self._name = _name

    name = property (get_name, set_name)

    @property
    def year(self):
        print("getting year")
        return self._year

    @year.setter
    def year(self, year):
        print("setting year")
        self._year = year
