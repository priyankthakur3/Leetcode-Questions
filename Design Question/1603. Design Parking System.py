class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.park_arr = [0 , big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.park_arr[carType] <= 0:
            return False
        self.park_arr[carType] -= 1
        return True
        
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)