class BMW():
    def model(self):
        print("BMW Car Model : M3.")
        
    def topSpeed(self):
        print("Top speed BMW M3 GTR : 350 M/Fr.")
        
    def mileage(self):
        print("Mileage of BMW M3 GRE : 3 km/L.")

class Ferrari():
    def model(self):
        print("Ferrari Car Model : F8 Tributo.")
        
    def topSpeed(self):
        print("Top speed Ferrari F8 Tributo : 340 M/Fr.")
        
    def mileage(self):
        print("Mileage of Ferrari F8 Tributo : 5 km/L.")

o1 = BMW()
o2 = Ferrari()

for car in (o1, o2):
    car.model()
    car.topSpeed()
    car.mileage()
    print()