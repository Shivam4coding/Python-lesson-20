"""
1) Ask for the input size.
   a) Ask the user to enter any value of `n`.
   b) Suggest example values like 5, 10, or 50.
   c) Convert the input into an integer.

2) Show one-loop growth.
   a) Pause the program before running the loop.
   b) Use one for loop that runs from 0 to `n - 1`.
   c) Use `pass` because the loop is only counting steps.
   d) Print that the number of steps is `n`.

3) Identify linear time.
   a) Explain that one loop runs once per item.
   b) Label the time complexity as `O(n)`.
   c) Mention that this is called linear time.

4) Show nested-loop growth.
   a) Pause the program before running the nested loops.
   b) Use an outer loop that runs `n` times.
   c) Use an inner loop that also runs `n` times.
   d) Use `pass` because the loops are only counting steps.

5) Calculate quadratic steps.
   a) Multiply `n * n` to find the total number of steps.
   b) Print the value of `n`.
   c) Print the total steps for the nested loops.

6) Identify quadratic time.
   a) Explain that two nested loops run `n x n` times.
   b) Label the time complexity as `O(n^2)`.
   c) Mention that this is called quadratic time.

7) Print the loop-counting rule.
   a) Pause before showing the rule.
   b) Show that 0 loops means `O(1)`.
   c) Show that 1 loop means `O(n)`.
   d) Show that 2 nested loops mean `O(n^2)`.
"""

scores = [10, 20, 30, 40, 50]

n = int(input("Enter the number of scores: "))

print("One loop counts each score once. Press Enter to run ")

steps = 0

for score in scores:

 steps += 1

 print(" steps =", steps, " -> O(n) linear time")
 input("Nested loops count each pair of scores. Press Enter to run ")
 steps = 0
 for score in scores:
  for score2 in scores:

   steps += 1
   print(" steps =", steps, " -> O(n^2) quadratic time")
   input("Loop=counting rule: 0 loops = 0(1), 1 loop = O(n), 2 loops = O(n^2). Press Enter to run ")
   print("Loop-counting rule: 0 loops = O(1), 1 loop = O(n), 2 loops = O(n^2)")
   input("Press Enter to finish")

   