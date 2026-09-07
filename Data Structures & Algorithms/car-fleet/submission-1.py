class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        fleets = 0
        fleet_time = 0

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i],time))

        cars.sort(reverse=True, key=lambda x: x[0])

        for _, time in cars:
            if time > fleet_time:
                fleets += 1
                fleet_time = time
        
        return fleets