from unittest import TestCase
from algorithms.mergesort import mergesort
import random
import time

class TestMergeSort(TestCase):
    def test_resort(self):
        seed = time.time_ns()
        random.seed(seed)
        for i in range(12):
            unsorted = [round(random.random(), 4) for _ in range(i**2)]
            self.assertEqual(
                mergesort(unsorted), mergesort(mergesort(unsorted)), 
                f"\nResorting the following list produced a different list with seed {seed}:\n{unsorted}"
            )