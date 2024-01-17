# Rod Cutting Problem

We start out with a given length of rod that we are selling. This problem gives you multiple ways to cut the rod and make the most money based on a fixed number of length allowed to cut and the price of those cuts.

### For example:

Starting with a 10m Rod.
Below is the allowed cut lengths and price per cut at that length.

| length | Price |
| ------ | ----- |
| 3      | 1.80  |
| 4      | 2.00  |

1. Sequence of decision
2. If i commit to one decision at the current stage.
3. The final solution involves solving **2)** optionally and combining with original decision.

## Memoization

1. ID the optimal substructure
2. Write down a recurrence for the optimal value.
3. Memoize

When using duplicate for example multiple `maxRev(3)` memoize using a memo table so you can call the memo table instead of computing `maxRev(3)` each time.
