from __future__ import annotations
from data_structures.referential_array import ArrayR
from data_structures.abstract_heap import AbstractHeap, T
from typing import Literal, Iterable
from abc import abstractmethod

HeapOrders = Literal['min', 'max']

class UnorderedArrayHeap(AbstractHeap[T]):
    def __init__(self, max_items:int):
        if not max_items >= 0:
            raise ValueError("Heap must store 0 or more items.")
        self.__array = ArrayR[T](max_items + 1)
        self.__length = 0

    def __len__(self):
        return self.__length

    def peek(self) -> T:
        if self.__length == 0:
            raise IndexError("Cannot peek from empty heap.")
        return self.__array[1]
    
    @abstractmethod
    def _should_rise(self, below:T, above:T) -> bool:
        pass
        
    @abstractmethod
    def _should_sink(self, above:T, below:T ) -> bool:
        pass
        
    def __get_child_index(self, k:int) -> int | None:
        k2 = k*2
        if k2 > len(self):
            return None
        elif k2 == len(self):
            return k2
        else:
            left = self.__array[k2]
            right = self.__array[k2 + 1]

            if self._should_sink(left, right):
                #if left is put on top it is unstable, so right should be put on top
                return k2 + 1
            return k2

    def __get_parent_index(self, k:int) -> int | None:
        if k == 1:
            return None
        return k // 2

    def _rise(self, k:int) -> None:
        rising_item = self.__array[k]
        
        while (parent_i := self.__get_parent_index(k)) and self._should_rise(rising_item, self.__array[parent_i]):
            self.__array[k] = self.__array[parent_i]
            k = parent_i
            
        self.__array[k] = rising_item

    def add(self, item:T) -> None:
        if len(self) == len(self.__array) - 1:
            raise ValueError("Cannot add to full heap.")
        
        self.__length += 1
        self.__array[len(self)] = item
        self._rise(len(self))

    def _sink(self, k:int) -> None:
        sinking_item = self.__array[k]
        while (child_i := self.__get_child_index(k)) and self._should_sink(sinking_item, self.__array[child_i]):
            self.__array[k] = self.__array[child_i]
            k = child_i

        self.__array[k] = sinking_item

    def extract_root(self) -> T:
        if self.__length == 0:
            raise ValueError("Cannot extract_root from empty heap.")
        res = self.__array[1]
        self.__array[1] = self.__array[len(self)]
        self.__length -= 1
        self._sink(1)
        return res
        
    @classmethod
    @abstractmethod
    def heapify(cls, items:Iterable[T], heap:UnorderedArrayHeap[T]) -> UnorderedArrayHeap[T]:
        try:
            length = len(items)
            array = ArrayR(length + 1)
            for i, item in enumerate(items):
                array[i + 1] = item
            

        except TypeError:
            def resize(array):
                new_array = ArrayR(len(array) * 2)
                for i in range(len(array)):
                    new_array[i] = array[i]
                return new_array
            
            array = ArrayR(2)
            for i, item in enumerate(items):
                if i + 1 >= len(array):
                    array = resize(array)
                array[i + 1] = item
            
            length = i + 1
        
        heap.__array = array
        heap.__length = length
        

        for i in range(len(heap) // 2, 0, -1):
            heap._sink(i)
        
        return heap


