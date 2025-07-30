# stack_waiter

You are a waiter at a party. There is a pile of numbered plates in stack `A0`. Create an empty `answers` array. At each iteration, `i`, remove each plate from the top of the `A(i-1)` stack in order. Determine if the number on the plate is evenly divisible by the `ith` prime number. If it is, stack it in pile `Bi`. Otherwise, stack it in stack `Ai`. Store the values in `Bi` from top to bottom in `answers`. Notice that future iterations will be pulling from the just created `Ai` stack. Once the required number of iterations is complete, store the remaining values in `Ai` in `answers`, again from top to bottom. Return the `answers` array.

## Function Description

Input:

* Array of int for number on the plates
* int q for the number of iterations

Output:

* Array of int of the plate numbers after processing.

## Constraints

1 <= n <= 10^4
2 <= A0[i] <= 10^4
1 <= q <= 1200
