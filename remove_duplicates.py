def remove_duplicates(items):
    """
    Removes duplicate values from a list.
    Currently breaks when mixed types appear (e.g., int + str).
    """
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
