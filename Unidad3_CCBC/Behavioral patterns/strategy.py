# autor:Carla del Carmen Barcenas Castillo
# Grupo: GITI9072
# nombre: behaviral patterns

import types

class Strategy:

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # if a reference to a function is provided, replace the execute() method with the given function.

    def execute(self):  # This gets replaced by another version if another strategy is provided.
        print("{} is used!".format(self.name))


# Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))


# Replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))

#  Let's create our default strategy
s0 = Strategy()
# Let's execute our default strategy
s0.execute()

# Let's create de first variation of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)
# Let's set its name
s1.name
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_one)
s2.name = "Strategy One"
s1.execute()  

s2 = Strategy(strategy_two)
s2.name = "Strategy_two"
s2.execute()