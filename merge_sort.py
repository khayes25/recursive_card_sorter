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

    def sort(list) :
        merge_sort(list, 0, len(list) - 1)

    """
    Merges two partitions of an array together, in the correct order.
    """
    def merge(list, left, middle, right) :
        lower_counter = 0
        upper_counter = 0
        merge_counter = left

        lower_size = middle - left + 1
        upper_size = right - middle

        temp_lower = []
        temp_upper = []

        for i in range(0, lower_size) :
            temp_lower.insert(i, list[left + 1])

        for i in range(0, upper_size) :
            temp_upper.insert(i, list[middle + 1 + I])

        while(lower_counter < lower_size and upper_counter < upper_size) :
            if(temp_lower[lower_counter] <= temp_upper[upper_counter]) :
                list[merge_counter] = temp_lower[lower_counter]
                lower_counter += 1

            else :
                list[merge_counter] = temp_upper[upper_counter]
                upper_counter += 1

            merge_counter += 1

        while(lower_counter < lower_size) :
            list[merge_counter] = temp_lower[lower_counter]
            lower_counter += 1
            merge_counter += 1

        while(upper_counter < upper_size) :
            list[merge_counter] = temp_upper[upper_counter]
            upper_counter += 1
            merge_counter += 1

