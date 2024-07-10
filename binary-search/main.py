def binary_search(list, element):
    # Define the right and left indexes
    left_index = 0
    right_index = len(list) - 1

    while left_index <= right_index:
        # Get the middle index
        middle_index = (left_index + right_index) // 2

        # Get the middle element (pivot)
        pivot = list[middle_index]

        # Validate the pivot element
        if pivot == element:
            return True
        elif pivot > element:
            # If the pivot is grether than the element then discard the left elements
            right_index = middle_index - 1
        elif pivot < element:
            # If the pivot is grether than the element then discard the right elements
            left_index = middle_index + 1
    return False


list = [29, 44, 6, 11, 10, 89, 12, 45, 17, 18, 25, 5, 56]
list.sort()
print(f"list = {list}")

element = 10
is_element_found = binary_search(list, element)
print(f"is_element_found = binary_search(list, {element})")
print(is_element_found)

element = 20
is_element_found = binary_search(list, element)
print(f"is_element_found = binary_search(list, {element})")
print(is_element_found)
