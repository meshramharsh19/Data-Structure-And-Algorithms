class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        checkList = flowerbed.copy()
        if n == 0 :
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                    flowerbed[i]=1
                    n -= 1
                if n == 0:
                    break
               

        if n == 0 :
            return True
        else:
            return False