# 1603. Design Parking System


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        
        self.big_count = big
        self.medium_count = medium
        self.small_count = small


    def addCar(self, carType: int) -> bool:
        
        if carType == 1:
            if self.big_count > 0:
                self.big_count -= 1
                return True
            else:
                return False

        if carType == 2:
            if self.medium_count > 0:
                self.medium_count -= 1
                return True
            else:
                return False

        if carType == 3:
            if self.small_count > 0:
                self.small_count -= 1
                return True
            else:
                return False




# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(big=1, medium=1, small=0)
print(obj.addCar(carType=1))
print(obj.addCar(carType=2))
print(obj.addCar(carType=3))
print(obj.addCar(carType=1))

# [null, true, true, false, false]
# Explanation
# ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
# parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
# parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
# parkingSystem.addCar(3); // return false because there is no available slot for a small car
# parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.
 

