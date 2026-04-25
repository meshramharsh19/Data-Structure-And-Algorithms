class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        altitude = 0 
        biggernumber = 0
        for i in range (len(gain)):
            altitude = altitude + gain[i]
            if altitude > biggernumber :
                biggernumber = altitude
        return biggernumber
        