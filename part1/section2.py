from typing import List


def reverse_string(arr: List[str]) -> List[str]:
    # Initialize left and right pointers with 0 and length of array
    left_ptr, right_ptr = 0, len(arr) - 1
    # Loop until both pointers are at the same point or pass each other
    while left_ptr <= right_ptr:
        # Swap elements in array that left and right pointers point to
        arr[left_ptr], arr[right_ptr] = arr[right_ptr], arr[left_ptr]
        # Increment left pointer
        left_ptr += 1
        # Decrement right pointer
        right_ptr -= 1
    # Returns reversed array
    return arr
