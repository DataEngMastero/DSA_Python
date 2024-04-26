# Dynamic Programming

Dynamic Programming is enhanced recursion where problem is solved via recursion and add storage.

How to identify if a problem can be solved with DP or not ?
1. If you are given a choice (ex: to include element or not)
2. If you are asked to find optimal solution (ex: min, max, largest, smallest, etc.)

Right way of solving DP ?
1. Write recursion solution = call same function in smaller input.
    Base Condition - Write the smallest possible valid input
    Write Choice Diagram Code
2. Memoization
3. Top-Down Solution

Types of DP Problems
1. 0-1 Knapsack Problems -
You are given a knapsack and set of items with their value and weight given. The goal is to find max profit that can be added in our knapsack for given target weight. Here, given item can either be included or excluded.

    i. Subset Sum - Given an array of integers and sum. Check if subset is present with the target sum.
    ii. Equal Sum Partition - Check if the given array can be partitioned into two subsets of equal sum.
    iii. Count of Subset Sum - Return count of subsets for a given sum in an array
    iv. Minimum Subset Sum Difference - Split the array into two subsets such that absolute difference of their sum is minimum.
    v. No. of Subset for given sum - Divide Array into 2 subsets, such that sum of two subset is equal to given difference. Return the count of subset found.
    vi. Target Sum - No of Combinations via which target sum can be accomplished

2. Unbounded Knapsack Problems -
You are given a knapsack and set of items with their values and weights given. Here, one item can be chosed multiple times.

    i. Rod Cutting - Maximise the profit of a rod by cutting into lengths (with given prices)
    ii. Coin Channge I  - Given set of coins and sum, find the number of ways we can make sum where one coin can be used multiple times.
    iii. Coin Change II - 
    iv. Maximum Ribbon Cut - 
