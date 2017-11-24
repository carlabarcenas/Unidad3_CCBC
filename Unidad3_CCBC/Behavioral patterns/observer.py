# autor:Carla del Carmen Barcenas Castillo
# Grupo: GITI9072
# nombre: behaviral patterns

class Subject(object):  # Represents what being 'observed'

    def __int__(self):
        self.observers = []  # This where references to al the observers are being kept
        # Note that this is a one-to-many relationship: there will be ome subject to be observed by multiple _observers

    def attach(self, observer):
        if observer not in self._observers:  # if the observer is not already in the observers list
            self._observers.append(observer)  # append the observer to the list

    def detach(self, observer):  # Simply remove the observed
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:  # For all the observers in the list
            if modifier != observer:  # don't notify the observer who is actually updating the temperature
                observer.update(self)  # Alert the observers!


class Core(Subject):  # inherits from the Subject class

    def __init__(self, name=""):
        Subject.__init__(self)
        self.name = name  # set the name of the core
        self._temp = 0  # initialize the temperature of the core

    @property  # Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter  # Setter that sets of the core temperature
    def temp(self, temp):
        self._temp = temp
        # Notify the observers whenever somebody changes the core temperature


class TempViewer:
    def update(self, subject):  # Alert method that is invoked when the notify() method in a concrete subject is invoked
        print("Temperature Viewer: {} has temperature {}".format(subject._name, subject._temp))


# Let's create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

# Let's attach our observers to the first core
c1.attach('v1')
c2.attach('v2')

# Let's change the temperature of our first core
c1.temp = 80
c2.temp = 90
