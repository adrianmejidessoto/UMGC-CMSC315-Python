Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

## Completed Implementation

I modeled a campus IT laptop inventory using integer asset IDs. I completed every starter TODO block while retaining the original instructions and requirements as reference comments and docstrings. I replaced the executable TODO placeholder messages with working demonstrations and explanatory output.

I implemented `linear_search(lst, target)` by scanning from the first element to the last. It returned the first matching index or -1. I implemented `binary_search(lst, target)` with inclusive low and high bounds. After checking the midpoint, I set low to midpoint + 1 or high to midpoint - 1. Both functions retained their original two-argument calls and integer return values. I added an optional `stats` dictionary to count elements examined.

## Tests and Results

I ran `python unit5_discussion.py` and verified every demonstration with explicit checks that raised AssertionError on an incorrect result.

| Dataset and target | Linear index | Binary index | Linear elements examined | Binary elements examined |
|---|---:|---:|---:|---:|
| Seven IDs, existing 1060 | 5 | 5 | 6 | 2 |
| Seven IDs, missing 1065 | -1 | -1 | 7 | 3 |
| 100000 IDs, existing 199999 | 99999 | 99999 | 100000 | 17 |
| 100000 IDs, missing 200000 | -1 | -1 | 100000 | 17 |

I tested an empty list, single-element matches and misses, first and last positions, targets below and above the range, and duplicate values. Empty input returned -1 without accessing an element. Missing targets returned -1. Linear search returned the first duplicate, while binary search returned a matching duplicate without promising the first occurrence.

I also checked both implementations against Python's list membership behavior over generated sorted lists, duplicates, negative values, and missing values. All verification cases passed. The run output was saved in `run_output.txt`.

## Performance Analysis and Preconditions

I compared elements examined, rather than wall-clock execution times or individual comparison operators. The large-list examples demonstrated O(n) worst-case linear search and O(log n) worst-case binary search. Both iterative algorithms used O(1) auxiliary search space. I built the large dataset before searching, so its construction was not counted as search work.

I used comparable integer IDs and supplied sorted lists to binary search. I did not silently sort inside the search function because that would add preparation cost and change the returned index's meaning. Binary search was not reliable on unordered data or data without consistent comparisons. Its logarithmic element-access performance assumed efficient indexing. A linked list would not provide the same access efficiency.

## Real World Application

I searched an unsorted arrival list for asset ID 1070 with linear search and obtained arrival index 2. I sorted a separate copy and found the same ID at sorted index 3 with binary search. This showed why indices had to be interpreted relative to the list searched. A one-time lookup could favor scanning instead of paying O(n log n) to sort first. Repeated lookups could justify maintaining sorted inventory. I used IDs as lookup keys; I did not claim that sorting IDs alone preserved complete laptop records.

## Completed Discussion Board Reflection

For this discussion, I implemented linear and binary search in a laptop inventory example. Linear search checked asset IDs in arrival order, while binary search used a sorted list. Both returned an index for a match and -1 when an ID was absent.

I learned how search boundaries and data organization affected correctness and efficiency. The main implementation challenge was updating the binary search boundaries without skipping candidates or repeating the middle element. I addressed this by excluding the checked midpoint and testing empty lists, single-element lists, missing IDs, duplicates, and both endpoints.

In the 100,000-ID dataset, finding the last ID examined 100,000 elements with linear search and 17 with binary search. Binary search halved the remaining interval, giving O(log n) worst-case search time instead of O(n). These counts measured examined elements rather than execution time.

Linear search remained appropriate for one lookup in an unsorted arrivals list because sorting first would add preparation work. Repeated searches could justify that cost. Binary search could not reliably search unordered data or values without consistent comparisons. Its usual efficiency also depended on fast indexed access. Sorting changed positions, so I reported indices relative to the searched list.
