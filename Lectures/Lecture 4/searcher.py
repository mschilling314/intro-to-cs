def linear_search(arr: list[float], target: float) -> int:
    """
    This function will search each element of a list of floats until it finds the target.  Returns the leftmost index of target (if target is present multiple times) or -1.

    Inputs:
    ------
    (param) arr: a list of floating numbers you'd like to search
    (param) target: the number you'd like to find in the list

    Output:
    ------
    An integer that is either the leftmost index where you can find target in the arr, or -1 if target is not in arr.
    """
    x = len(arr)
    for i in range(x):
        if arr[i] == target:
            return i
    return -1