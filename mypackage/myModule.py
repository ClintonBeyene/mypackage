def top_n(items, n):
    """Return the top n items in an array, in decending order.

    Args:
        items (array): List or array-like object containing numerical values.
        n (int): number of top items to return.

    Returns: 
        array: The top n items in the array, in descending order.

    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]    
    """
    for i in range(n):
        for j in range(len(items) - 1 - i):
            if items[j] < items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    # Get the last two items 
    top_n_items = items[-n:]

    # Return in decending order 
    return top_n_items[::-1]

