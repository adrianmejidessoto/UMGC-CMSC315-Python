# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Implementation

I used a BST to model a campus IT inventory index for laptop asset IDs. I stored one ID per node. Recursive insertion put smaller IDs in the left subtree and larger IDs in the right subtree. It created a node at the first empty position and kept a single entry for each ID.

I inserted `1400, 1200, 1600, 1100, 1300, 1500, 1700` in that order to populate both sides of the tree. The in-order traversal visited the left subtree, the current node, and the right subtree. It returned `1100, 1200, 1300, 1400, 1500, 1600, 1700`.

## Verification

I ran `python unit4_discussion.py` from this folder. The search found `1100` and `1600`. It did not find `1250`, which fell between stored IDs, or `1800`, which exceeded the largest ID. The empty tree returned an empty traversal and a failed search. Inserting `1400` again left the sorted inventory unchanged.

## Performance

I used the BST ordering rule to choose a single branch at each search step. The sample tree had three levels, so searching for any stored ID took at most three node visits. Inserting the same seven IDs in ascending order would have created a chain. Finding the largest ID in that chain would have required seven node visits, similar to a linear search.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.