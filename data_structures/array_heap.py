from __future__ import annotations
from data_structures.referential_array import ArrayR
from data_structures.unordered_array_heap import UnorderedArrayHeap, T
from typing import Literal, Iterable

HeapOrders = Literal['min', 'max']

class ArrayHeap(UnorderedArrayHeap[T]):
    MAX_ORDERING = 0
    MIN_ORDERING = 1

    def __init__(self, max_items:int, ordering: HeapOrders):
        UnorderedArrayHeap.__init__(self, max_items)

        if ordering == 'min':
            self.__heap_order = ArrayHeap.MIN_ORDERING
        elif ordering == 'max':
            self.__heap_order = ArrayHeap.MAX_ORDERING
        else:
            raise ValueError("Array heap recieved invalid heap ordering: " + ordering)
    
    def _should_rise(self, below:T, above:T) -> bool:
        if self.__heap_order == ArrayHeap.MIN_ORDERING:
            return below < above
        else:
            return below > above 
        
    def _should_sink(self, above:T, below:T ) -> bool:
        if self.__heap_order == ArrayHeap.MIN_ORDERING:
            return above > below
        else:
            return above < below
        
    @classmethod
    def heapify(cls, items: Iterable[T], ordering:HeapOrders) -> ArrayHeap[T]:
        """ Construct a heap from an iterable of items. 
        returns: A heap containing all of the items in the iterable.
        complexity: O(n) where n is the number of items in the iterable.
        """
        return ArrayHeap(0, ordering)._heapify(items)
    
    def __str__(self):
        return "ArrayHeap(" + ("min, " if self.__heap_order == ArrayHeap.MIN_ORDERING else "max, ") + UnorderedArrayHeap.__str__(self) + ')'
