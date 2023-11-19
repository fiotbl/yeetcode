class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        fleet, currTime = 0, 0
        
        for car in sorted(cars, reverse=True):
            time = (target - car[0])/car[1]
            if time > currTime:
                fleet += 1
                currTime = time
        
        return fleet