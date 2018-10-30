class Airline():
    _all = []

    def __init__(self, name, year):
        Airline._all.append(self)
        self._name = name
        self._year = year

# simple way of getters and setters:
    def get_name(self):
        print("Getting name")
        return self._name

    def set_name(self, name):
        print("Setting name")
        self._name = _name

    name = property (get_name, set_name)

#fancy way of getters and setters:
    @property
    def year(self):
        print("getting year")
        return self._year

    @year.setter
    def year(self, year):
        print("setting year")
        self._year = year

    @classmethod
    def all(cls):
        print(cls)
        return Airline._all

    @classmethod
    def all_names(self):
        pass #would move through Airline._all and print out all the names for us
