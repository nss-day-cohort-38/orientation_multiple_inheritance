from habitats import Habitat
from movements import ISwimming

class Aquarium(Habitat):
    def __init__(self, name):
        super().__init__(name)
        
    # Duck typing, the Pythonic way
    def add_animal(self, animal):
        try:
            if animal.swim_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(f'{animal} can\'t swim, so please do not try to put it in the {self.name} habitat')
            
    # Not the Pythonic way!!!        
    # def add_animal(self, animal):
    #     if isinstance(animal, ISwimming):
    #         self.animals.add(animal)
    #     else:
    #         print(f'{animal} can\'t swim, so please do not try to put it in the {self.name} habitat')
