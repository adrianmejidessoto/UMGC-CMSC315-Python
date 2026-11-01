# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?
## Implementation Summary

I completed the list operations in `unit3_discussion.py` and used a song playlist as a real-world example. I preserved the original TODO instructions and added comments explaining the implementation.

I implemented `insert_at` using `list.insert`, `delete_at` using index validation and `list.pop`, and `search_value` using a sequential loop. The search returned the first matching index or -1 when no match existed. Deletion returned None for an invalid index.

## Tests and Results

I tested insertions and deletions at the beginning, middle, and end of the playlist. I printed the playlist after each change and displayed each removed song.

I searched for Song A and received index 0. Searching for Missing Song returned -1. I also tested deletion at an index equal to the list length, deletion from an empty list, searching an empty list, and insertion into an empty list. Invalid deletions returned None, the empty search returned -1, and insertion produced a list containing First Song.

The program finished with exit code 0, and the displayed results matched the expected behavior.

## Performance and Application

The playlist demonstrated how an application maintained an ordered collection while allowing songs to be inserted, removed, and located.

I documented that beginning and middle insertions required shifting later elements and took O(n) time. End insertion took amortized O(1), although resizing could take O(n). Deleting from the beginning or middle also required shifting elements, while removing the last item took O(1). Sequential searching took O(n) in the worst case.

I identified frequent insertions and deletions at known node positions as a situation where a linked list could outperform an array-based list. This advantage depended on already having the required node references; locating a position could still take O(n).