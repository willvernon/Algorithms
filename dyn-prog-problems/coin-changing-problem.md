# Coin Changing Problem

The coin change problem is a classic problem in computer science, often used to illustrate the concept of dynamic programming. There are two main variation of the problem:

1. The first variation asks for the total number of combinations of coins that can make up a given amount. For example, given coins of 1 cent, 5 cents, and 10 cents, how many combinations of these coins can make up 8 cents? The answer would be 2: one way is to use eight 1-cent coins, and the other way is to use three 1-cent coins and one 5-cent coin.
2. The second variation, also known as the change-making problem, seeks the minimum number of coins that add up to a given amount. For instance, if you have coins of 1, 5, and 10 cents, what is the least number of coins you can use to make 8 cents? The answer would be 2: one 5-cent coin and three 1-cent coins.

These problems are typically solved using dynamic programming, a method that breaks down a complex problem into simpler sub-problems, solves each sub-problems just once, and stores their solutions - ideally in a table structure. The solutions to these sub-problems are then combined to give a solution to the original problem.
