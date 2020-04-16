from movements import IWalking, ISwimming

class Penguin(IWalking, ISwimming):
    def __init__(self, name):
        IWalking.__init__(self)
        ISwimming.__init__(self)
        self.name = name
        
    def __str__(self):
        return f"{self.name} the Penguin"
    
    # Method overriding, in object-oriented programming, is a language feature that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its superclasses or parent classes.
    def run(self):
        print(f'{self} waddles')
