class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort()
        while cars:
            print(cars)
            nextPos, nextSp = cars.pop()
            nextETA = (target - nextPos) / nextSp
            print(nextETA)
            while cars and nextETA >= (target - cars[-1][0]) / cars[-1][1]:
                cars.pop()
            res += 1
        return res
        
