class Vehicle:
    def __init__(self, max_speed, mileage, model):
        self.max_speed=max_speed        
        self.mileage=mileage        
        self.model=model
class Bus(Vehicle):
    pass
School_bus=Bus("120", "40", "Volvo v-15")
print("Model:",School_bus.model,"\n""Max_speed:",School_bus.max_speed,"\n""Mileage:",School_bus.mileage)        