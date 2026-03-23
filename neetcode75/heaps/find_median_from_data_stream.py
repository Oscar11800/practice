from neetcode75.test_runner import assert_equal, run_tests
import heapq
"""
Find Median From Data Stream

The median is the middle value in a sorted list of integers. For lists of
even length, there is no middle value, so the median is the mean of the two
middle values.

For example:
For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data
  structure.
- double findMedian() returns the median of all elements so far.

Example 1:
Input:
["MedianFinder", "addNum", "1", "findMedian", "addNum", "3", "findMedian",
 "addNum", "2", "findMedian"]
Output:
[null, null, 1.0, null, 2.0, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder()
medianFinder.addNum(1)    # arr = [1]
medianFinder.findMedian() # return 1.0
medianFinder.addNum(3)    # arr = [1, 3]
medianFinder.findMedian() # return 2.0
medianFinder.addNum(2)    # arr = [1, 2, 3]
medianFinder.findMedian() # return 2.0

Constraints:
-100,000 <= num <= 100,000
findMedian will only be called after adding at least one integer to the data
structure.
"""


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        if self.min_heap and self.max_heap and -self.max_heap[0] >= self.min_heap[0]:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        while len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            # balance the tree
        while len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            if len(self.max_heap) > len(self.min_heap):
                return -self.max_heap[0]
            else:
                return self.min_heap[0]


def test_example1():
    mf = MedianFinder()
    mf.addNum(1)
    assert_equal(mf.findMedian(), 1.0)
    mf.addNum(3)
    assert_equal(mf.findMedian(), 2.0)
    mf.addNum(2)
    assert_equal(mf.findMedian(), 2.0)


# Run: python3 -m neetcode75.heaps.find_median_from_data_stream
if __name__ == "__main__":
    run_tests()
