class Solution:
    def wateringPlants(self, plants, capacity):
        steps = 0
        amount_water = capacity
        for i in range(len(plants)): 
            if plants[i] > amount_water: 
                steps += 2*i
                amount_water = capacity
            amount_water -= plants[i]
            steps += 1
        return steps