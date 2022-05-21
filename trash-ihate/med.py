import bisect

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.nums , num)

    def findMedian(self) -> float:
        if len(self.nums)%2 != 0:
            med = len(self.nums)//2
            return self.nums[med]
        
        med , med2 = len(self.nums)//2 , ( len(self.nums)//2 - 1)
        return ( self.nums[med] + self.nums[med2] )/2
        

# if __name__ == "__main___":
m1 = MedianFinder()
m1.addNum(6)
m1.addNum(10)
m1.addNum(2)
# m1.addNum(6)
# m1.addNum(5)



print(m1.findMedian())
    # m1.addNum(6)