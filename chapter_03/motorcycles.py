motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
remove = motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

motorcycles.insert(3, True)
print(motorcycles)

del motorcycles[-2]
print(motorcycles)

pop = motorcycles.pop(0)
print(pop)
