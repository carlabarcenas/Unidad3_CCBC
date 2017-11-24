#autor:Carla del Carmen Barcenas Castillo
#Grupo: GITI9072
#nombre: behaviral patterns

class Handler: #Abstract handLer
 """Abstract Handler"""

 def __init__(self, successor):
    self._successor = successor #Define who is the next handler


 def handle(self, request):
    handled = self._hand1e(request) #If bandied, stop here

    #Otherwise, keep going
    if not handled:
        self ._successor . handle(request)

 def _hand1e(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler): # Inherits from the abstract handler
    """Concrete handler 1"""
    def _hand1e(self, request):
        if 0 < request <- 10: # Provide a condition for handLing
            print("Request {} handled in handler 1".format(request))
            return True # Indicates that the request has been handLed

class DefaultHandler(Handler): # Inherits from the abstract handLer
    """Default handler"""

    def _handle(self, request):
     """If there is no handler available"""
        # No condition checking since this is a default handler
         print("End of chain, no handler for {}".format(request))
         return True  # Indicates that the request has been handled


class Client: # Using handled
    def _init_(self):
        self.handler = ConcreteHandler(DefaultHandler(None))  # Create handlers and use then in a sequence you want
                                                                    # Note that the default handler has no successor

    def delegate(self, request): # Send your requests one at time for handlers to handle
        for request in requests:
            self.handler.handle(request)

# create a client
c = Client()

# Create requests
requests = [2,5,30]

# Send the requests
c.delegate(requests)