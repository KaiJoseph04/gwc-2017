class Vehicle:
	
	def __init__(self, name):
        self.name = name
        self.wheels = 0
        self.ignition = False
        self.passengers = []


    def num_wheels(self, newWheels):
        self.wheels = newWheels
	
	
    def ignition(self, key):
	    self.ignition = key
		 
		
	def add_passenger(self, newPassenger):
		self.passengers.append(newPassenger)
		

def main():
    myCar = Vehicle("Corolla")
    myCar.num_wheels(4)	
    myCar.add_passenger("Kai")
		
		
if __name__ == '__main__':	
    main()