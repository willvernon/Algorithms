# The Knapsack Problem

The problem is named after a scenario where one is constrained by a fixed-size knapsack and needs to fill it with the most valuable combination of items. Each item has a specific weight and value, and the goal is to maximize the total value of items in the knapsack without exceeding its weight capacity.

There are several variations of the knapsack problem:

- **0/1 Knapsack Problem**: In this variation, each item can either be included in the collection or not, hence the name 0/1. The goal is to maximize the total value without exceeding the weight capacity.
- **Bounded Knapsack Problem**: This variation is similar to the 0/1 knapsack problem, but with an additional constraint that you can select a maximum of K items.
- **Unbounded Knapsack Problem**: In this variation, there is no limit on the number of each item you can include in the knapsack. The goal remains the same: to maximize the total value without exceeding the weight capacity.

Solves each sub-problem just once, and stores their solutions - ideally in a table structure. The solution to these sub-problems are then combined to give a solution to the original problem.
