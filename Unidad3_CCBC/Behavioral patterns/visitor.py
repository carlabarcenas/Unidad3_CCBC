# autor:Carla del Carmen Barcenas Castillo
# Grupo: GITI9072
# nombre: behaviral patterns

class House(object): # The class being visited
    def accept(self, visitor):
        """Interface to accept a visitor"""
        # Triggers the visiting operation!
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist): # Note that we now have a reference to the HVAC specialist object in the house object!


     def work_on_electricity(self, electrician):
       print(self, "worked on by", electrician) # Note that now have a reference to the electrician object in the house project!

    def __str__(self):
        """Simply return the class name when the house object is printed"""
        return self.__class__.__name__

class Visitor(object):
    """Abstract Visitor"""
    def __str__(self):
        """Simply return the class name when the Visitor object in printed"""
        return  self.__class__.__name__


class HvacSpecialist(Visitor):
    """Concrete visitor: HVAC specialist"""
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    """Concrete Visitor: Electrician"""
    def visit(self, house):
        house.work_on_electricity(self)

#create an HVAC specialist
hv = HvacSpecialist

#create an electrician
e = Electrician()

#create a house
home = House()

#Let the house accept the HVAC specialist and work on the house by invokin the visiti()

