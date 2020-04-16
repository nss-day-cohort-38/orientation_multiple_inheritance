from animals import Penguin, PaintedDog
from movements import IWalking
from habitats import Aquarium

bob = Penguin("Bob")

print(bob)
print(f"This is Bob: {bob}")

print("Bob's legs:", bob.legs)
bob.run()
print("Bob's swim speed: ", bob.swim_speed)
bob.swim()

jim = Penguin("Jim")

ralph = PaintedDog("Ralph")

seaworld = Aquarium("Sea World")
print(seaworld.__len__())

seaworld.add_animal(bob)
seaworld.add_animal(jim)
seaworld.add_animal(ralph)

print(seaworld.name)
for animal in seaworld.animals:
    print(animal)
    
