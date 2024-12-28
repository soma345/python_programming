import unittest
#from data_structure.heap import heap_kth_largest
from heap_kth_largest import findKthLargest

class TestSolution(unittest.TestCase):

    def test_findKthLargest(self):
        results= heap_kth_largest.findKthLargest([12,4,13,7,8,9,0])
        self.assertEqual(results,4)






if __name__ == '__main__':
    unittest.main()