"""
1) Set the input size.
   a) Store 10 in the variable `n`.
   b) Use this value to test different time complexity patterns.

2) Ask the user to predict.
   a) Explain that a double loop checks `n x n` pairs.
   b) Ask how many pairs are checked when `n = 10`.
   c) Store the user's guess.

3) Show constant time.
   a) Pause the program before running the formula example.
   b) Set `steps` to 1.
   c) Print that this is `O(1)`.
   d) Explain that constant time steps never change.

4) Show linear time.
   a) Pause the program before running the loop example.
   b) Start `steps` from 0.
   c) Use one for loop to run `n` times.
   d) Increase `steps` once for each item.
   e) Print that this is `O(n)`.

5) Show quadratic time.
   a) Pause the program before running the double loop example.
   b) Start `steps` from 0.
   c) Use an outer loop and an inner loop.
   d) Increase `steps` for every pair checked.
   e) Print the total steps and the user's guess.
   f) Show that this is `O(n^2)`.

6) Introduce two more notations.
   a) Pause the program before showing them.
   b) Print Big Omega as the best-case lower bound.
   c) Print Big Theta as the exact bound.
   d) Explain that Big Theta is used when best and worst cases match.
"""

# 01-big-o-notation.py

# Topic: Big-O Notation — each growth pattern has an official name

# Last class: Formula, Loop, Double Loop. Today each gets its Big-O name.

n = 10

guess = input("Double Loop at n = 10 checks n x n pairs. How many? ")
input("Formula: one calculation, done. Press Enter to run ")

steps = 1

print(" steps =", steps, " -> O(1) constant time -> steps never change")
input("Loop: one step per item. Press Enter to run ")

steps = 0

for i in range(n):

 steps += 1

print(" steps =", steps, " -> O(n) linear time -> steps grow with n")
input("Double Loop: checks every pair. Press Enter to run ")

steps = 0

for i in range(n):
 for j in range(n):

  steps += 1

print(" steps =", steps, " your guess:", guess, " -> O(n^2) quadratic time")
input("Two more notations. Press Enter ")
print(" Big Omega Ω -> best case lower bound")
print(" Big Theta Θ -> exact bound (worst = best)")