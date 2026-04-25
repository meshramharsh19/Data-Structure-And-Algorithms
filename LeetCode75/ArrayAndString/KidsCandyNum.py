class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        returnList = []
        maxiValue = max(candies)

        for i in range(len(candies)):
            newValue = candies[i] + extraCandies
            if newValue >= maxiValue:
                returnList.append(True)
            else:
                returnList.append(False)
        return returnList