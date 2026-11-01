"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Elements at and after the index shift one position to the right.
    # Beginning and middle insertions take O(n) time due to shifting.
    # End insertion takes amortized O(1), but resizing can take O(n).
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Validate the index to prevent errors and unintended deletions.
    # Invalid indexes, including deletion from an empty list, return None.
    if 0 <= index < len(lst):
        return lst.pop(index)
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Scan sequentially because the list is not assumed to be sorted.
    # Return the index of the first match; worst-case search takes O(n).
    for index, item in enumerate(lst):
        if item == value:
            return index
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Start with a playlist containing three songs.
    playlist = ["Song A", "Song B", "Song C"]
    print("Original playlist:", playlist)

    # Insert at the beginning, shifting all existing songs right.
    insert_at(playlist, 0, "Opening Song")
    print("After beginning insertion:", playlist)

    # Insert at the middle, shifting later songs right.
    middle = len(playlist) // 2
    insert_at(playlist, middle, "Middle Song")
    print("After middle insertion:", playlist)

    # Insert at the end without shifting existing songs.
    insert_at(playlist, len(playlist), "Closing Song")
    print("After end insertion:", playlist)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Remove the first song; later songs shift left.
    removed = delete_at(playlist, 0)
    print("Removed from beginning:", removed)
    print("Updated playlist:", playlist)

    # Remove the song at the current middle index.
    middle = len(playlist) // 2
    removed = delete_at(playlist, middle)
    print("Removed from middle:", removed)
    print("Updated playlist:", playlist)

    # Remove the last song without shifting other songs.
    removed = delete_at(playlist, len(playlist) - 1)
    print("Removed from end:", removed)
    print("Updated playlist:", playlist)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # Search for a song that remains in the playlist.
    index = search_value(playlist, "Song A")
    print("Search for Song A (existing): index", index)

    # A missing song returns -1 without changing the playlist.
    index = search_value(playlist, "Missing Song")
    print("Search for Missing Song (not found):", index)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # An index equal to the length is invalid for deletion.
    removed = delete_at(playlist, len(playlist))
    print("Invalid deletion returns:", removed)
    print("Playlist remains unchanged:", playlist)

    # Deleting from an empty playlist safely returns None.
    empty_playlist = []
    print("Delete from empty playlist:", delete_at(empty_playlist, 0))

    # Searching an empty playlist returns -1.
    print("Search empty playlist:", search_value(empty_playlist, "Song A"))

    # Inserting at index 0 works even when the playlist is empty.
    insert_at(empty_playlist, 0, "First Song")
    print("Insert into empty playlist:", empty_playlist)



if __name__ == "__main__":
    main()