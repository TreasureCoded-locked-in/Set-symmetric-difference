def symmetric_difference(set1, set2):
    """
    Finds the symmetric difference between two sets.

    The symmetric difference of two sets is the set of elements that exist in 
    either of the sets but not in both.

    Args:
        set1: The first set.
        set2: The second set.

    Returns:
        A new set containing the symmetric difference of the two sets.
    """
    return set1.symmetric_difference(set2)

# Example usage
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = symmetric_difference(set1, set2)
print("Symmetric difference:", result)  # Output: Symmetric difference: {1, 2, 5, 6}