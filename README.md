# Fish_Simulation
An simulation of fishes eating foods which spawn in random positions

fish:
  fishes are just displayed as circles with a line representing the velocity of fish. 
  a fish dont interact with other fishes.
  fishes has a vision to see foods , the velocity of fish is changed for every frame to eat the food or to turn the fish which is near the walls.
  fishes has health, velocity, size, position.

food:
  the foods are spawned at random position.
  the food is given to the fish that is in contact with food , after that the food is removed.
  if two or more fishes come in contact with food in a single frame then food is given to the fish which has minimum health. 
  a constant food count is maintained to keep fishes alive.

time complexity: O(fish_count*food_count)

language used : python

module used   : pygame module 
