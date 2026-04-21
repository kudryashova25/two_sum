import unittest
from typing import Optional, Tuple, List

def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


class TestTwoSum(unittest.TestCase):
    
    def test_basic_case(self):
        result = two_sum([2, 7, 11, 15], 9)
        self.assertEqual(result, (0, 1))
    
    def test_negative_numbers(self):
        result = two_sum([-3, 4, 3, 90], 0)
        self.assertEqual(result, (0, 2))
    
    def test_same_numbers(self):
        result = two_sum([5, 5, 11, 15], 10)
        self.assertEqual(result, (0, 1))
    
    def test_zero_target(self):
        result = two_sum([0, 4, 3, 0], 0)
        self.assertEqual(result, (0, 3))
    
    def test_no_solution(self):
        result = two_sum([1, 2, 3], 10)
        self.assertIsNone(result)
    
    def test_empty_list(self):
        result = two_sum([], 5)
        self.assertIsNone(result)
    
    def test_single_element(self):
        result = two_sum([5], 5)
        self.assertIsNone(result)
    
    def test_large_numbers(self):
        result = two_sum([1000000, 2000000, 3000000], 5000000)
        self.assertEqual(result, (1, 2))
    
    def test_multiple_pairs_first_returned(self):
        result = two_sum([1, 5, 8, 5], 10)
        self.assertEqual(result, (1, 2))
    
    def test_duplicate_values_different_positions(self):
        result = two_sum([3, 2, 3], 6)
        self.assertEqual(result, (0, 2))


if __name__ == "__main__":
    unittest.main()