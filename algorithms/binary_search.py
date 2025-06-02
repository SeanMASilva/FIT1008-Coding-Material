from __future__ import annotations
from data_structures.referential_array import ArrayR
from data_structures.array_list import ArrayList
from typing import TypeVar

T = TypeVar("T")

# We are defining a type, and we are saying it can be either an ArrayList or an ArrayR.
ListOrArray = TypeVar("ListOrArray", ArrayList[T], ArrayR[T])


def binary_search(my_list: ListOrArray, target_item: T) -> int:
    """
    Utilise the binary search algorithm to find the index where a particular element would be stored.
    This implementation assumes the item is in the list and the list is sorted.

    Args:
        my_list: the list to be searched.
        target_item: the target element to be found.

    Returns:
        The index at which either:
            * This item is located, or
            * ValueError if the item cannot be found.

    Complexity:
        Best Case Complexity: O(1), when middle index contains item.
        Worst Case Complexity: O(log(N)), where N is the length of my_list.
    """
    def _binary_search_aux(my_list, target_item, lo, hi) -> int:
        """
        Auxiliary method used by binary search.

        Args:
            my_list and target_item are the same as the outer function.
            The range of indices is [inclusive, exclusive):
            lo (int): Smallest index where the return value could be.
            hi (int): One after the largest index where the return value could be.
        """
        # If the range is empty, item is not in the list.
        if lo >= hi:
            raise ValueError(f"{target_item} not found in the list.")

        # If there is only one item in the range, must be the item we are looking for.
        if hi - lo == 1:
            if my_list[lo] == target_item:
                return lo
            raise ValueError(f"{target_item} not found in the list.")
        
        # Otherwise, we have more than one item in the range.
        # Calculate the middle index.
        mid = (hi + lo) // 2

        # Compare the middle item with the target item.
        if my_list[mid] > target_item:
            # Item would be before mid
            return _binary_search_aux(my_list, target_item, lo, mid)
        elif my_list[mid] < target_item:
            # Item would be after mid
            return _binary_search_aux(my_list, target_item, mid + 1, hi)
        elif my_list[mid] == target_item:
            # Item is at mid
            return mid
        
        # If we reach here, it means the comparison operator is not implemented correctly. Otherwise, at least
        # one of the conditions above should have been true.
        raise ValueError(f"Comparison operator poorly implemented {target_item} and {my_list[mid]} cannot be compared.")

    return _binary_search_aux(my_list, target_item, 0, len(my_list))
