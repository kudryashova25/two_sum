"""
Решение задачи "Сумма двух чисел"
"""
from typing import List, Optional, Tuple

def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Решение перебором (для понимания, но не для продакшена)
    Сложность O(n²)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


if __name__ == "__main__":
    # Простая проверка
    print(two_sum([2, 7, 11, 15], 9))  # (0, 1)