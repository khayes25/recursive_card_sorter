"""
Merge Sort Algorithm
"""

#Class Header
class Merge_Sort :
    def merge_sort(list, left, right) :
        if(left < right) :
            middle = (left + right) / 2

            merge_sort(list, left, middle)
            merge_sort(list, middle + 1, right)

            merge(list, left, middle, right)

    """
    Merges two partitions of an array together, in the correct order.
    """
    def merge(list, left, middle, right) :
        lower_counter = 0
        upper_counter = 0
        merge_counter = left

        lower_size = middle - left + 1
        upper_size = right - middle
        

