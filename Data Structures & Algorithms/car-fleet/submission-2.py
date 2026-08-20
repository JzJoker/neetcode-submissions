class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, sp) for pos, sp in zip(position, speed)]
        cars.sort(reverse = True)
        fleets = 1
        nextETA = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(cars)):
            currCar = cars[i]
            currETA = (target - currCar[0]) / currCar[1]
            if  currETA > nextETA:
                fleets += 1
                nextETA = currETA
        return fleets
        
