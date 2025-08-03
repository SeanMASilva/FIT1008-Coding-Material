from __future__ import annotations
from data_structures.unordered_array_heap import UnorderedArrayHeap, T
from typing import Iterable

class MaxArrayHeap(UnorderedArrayHeap[T]):
    def _should_rise(self, below:T, above:T) -> bool:
        return below > above

    def _should_sink(self, above:T, below:T ) -> bool:
        return above < below
    
    def extract_max(self) -> T:
        return self.extract_root()
    
    @classmethod
    def heapify(cls, items: Iterable[T]) -> MaxArrayHeap[T]:
        empty_heap = MaxArrayHeap(0)
        return  UnorderedArrayHeap.heapify(items, empty_heap)