"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target, stats=None):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Count elements examined, not individual Python comparison operators.
    if stats is not None:
        stats["examined"] = 0
    # In the worst case every element is visited, giving O(n) time.
    for index, value in enumerate(lst):
        if stats is not None:
            stats["examined"] += 1
        if value == target:
            return index
    return -1


def binary_search(lst, target, stats=None):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    if stats is not None:
        stats["examined"] = 0
    low, high = 0, len(lst) - 1
    # An empty list starts with high = -1, so no indexing occurs.
    while low <= high:
        middle = low + (high - low) // 2
        if stats is not None:
            stats["examined"] += 1
        if lst[middle] == target:
            return middle
        if lst[middle] < target:
            # Discard the middle and the lower half of the sorted interval.
            low = middle + 1
        else:
            # Discard the middle and the upper half; O(log n) iterations.
            high = middle - 1
    return -1



def demonstrate(label, items, target, expected):
    """Run both searches and verify the returned index against expectations."""
    print(f"{label}: size={len(items)}, target={target}")
    for name, search in (("Linear", linear_search), ("Binary", binary_search)):
        stats = {}
        result = search(items, target, stats)
        # For duplicate values, any index containing the target is valid.
        valid = result == expected if expected == -1 else (
            0 <= result < len(items) and items[result] == target
        )
        if not valid:
            raise AssertionError(f"{name}: unexpected index {result}")
        status = "not found" if result == -1 else f"found at index {result}"
        print(f"  {name}: {status}; elements examined={stats['examined']}")


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    # Sorted laptop asset IDs allow both algorithms to search the same data.
    small = [1010, 1020, 1030, 1040, 1050, 1060, 1070]
    demonstrate("Existing laptop", small, 1060, 5)
    demonstrate("Missing laptop", small, 1065, -1)
    # Both methods return the same index, but examine different counts.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # Prepare the list once; preparation is separate from search work.
    large = list(range(100000, 200000))
    demonstrate("Last laptop", large, 199999, 99999)
    demonstrate("Missing laptop", large, 200000, -1)
    print("Linear examined 100000 elements; binary examined 17 in each case.")
    print("Binary repeatedly halved the interval; linear visited each element.")
    print("Counts measured elements examined, not wall-clock execution time.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Empty and single-element lists check safe stopping conditions.
    demonstrate("Empty inventory", [], 1010, -1)
    demonstrate("Single laptop found", [1010], 1010, 0)
    demonstrate("Single laptop missing", [1010], 1020, -1)
    # Check both ends and absent values outside the sorted range.
    demonstrate("First position", small, 1010, 0)
    demonstrate("Last position", small, 1070, 6)
    demonstrate("Below minimum", small, 1000, -1)
    demonstrate("Above maximum", small, 1080, -1)
    demonstrate("Duplicate IDs", [1010, 1020, 1020, 1030], 1020, 1)
    print("Empty and missing searches returned -1; boundary searches found IDs.")
    print("Linear returned the first duplicate; binary returned a valid match.")

    # An unsorted arrival list demonstrates when linear search is appropriate.
    print("\n=== REAL-WORLD SCENARIO: LAPTOP INVENTORY ===")
    arrivals = [1060, 1010, 1070, 1030]
    print("Unsorted arrivals:", arrivals)
    print("Linear search for 1070, arrival index:", linear_search(arrivals, 1070))
    sorted_ids = sorted(arrivals)
    print("Sorted inventory:", sorted_ids)
    print("Binary search for 1070, sorted index:", binary_search(sorted_ids, 1070))
    print("Sorting changed the indices; each index belongs to the list searched.")
    print("One lookup can favor linear search because sorting costs O(n log n).")
    print("Repeated lookups can justify maintaining a sorted inventory.")
    print("Binary search requires consistent ordering and efficient index access.")
    print("Contract: lists contain comparable integer IDs; binary input is sorted.")
    print("All demonstration checks passed.")


if __name__ == "__main__":
    main()
