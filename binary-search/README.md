# Binary Search

The binary search finds the position of an element in an ordered list by comparing the element with the value in the middle of the list, if they are not equal, the half in which the value cannot be is eliminated and the search continues on the remaining half until the value is found.

For example, you want to find the 10 in the following list:

`[4, 6, 10, 12, 17, 25, 29]`

Compare the searched element with the central value: 10 < 12, it is smaller, then discard the right side.

`[4, 6, 10]`

Compare the searched element with the central value: 10 > 6, is greater, then discard the left side.

`[6, 10]`

Compare the searched element with the central value: 10 == 10, it is equal, so it was found.

If they would have been different, as there are no more elements left, the searched value is not in the list.

## Task

Write the function `binary_search(list, element)` that receives an ordered list and an element to be found.

The function should return `True` if it finds the element in the list using a binary search. If not found return `False`.

## Examples

```
> list = [29, 44, 6, 11, 10, 89, 12, 45, 17, 18, 25, 5, 56]
> is_element_found = binary_search(list, 10)
True
> is_element_found = binary_search(list, 20)
False
```
