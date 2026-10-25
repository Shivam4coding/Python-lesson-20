"""
1) Create the score list.
   a) Store the scores in a list named `scores`.
   b) Use comments to show the position of each item.
   c) Explain that linear search checks from left to right.

2) Display the list.
   a) Print the full list using `str(scores)`.
   b) Mention that the list size is 9.
   c) Pause the program using `input()`.

3) Ask for the target.
   a) Ask the user to enter a number to search for.
   b) Convert the input into an integer.
   c) Store the value in `target`.

4) Start the search.
   a) Pause before running the search.
   b) Create a `steps` counter.
   c) Start `steps` from 0.

5) Use linear search.
   a) Use a for loop to check each score.
   b) Increase `steps` by 1 for every check.
   c) Use `if` to check if the current score matches the target.
   d) Use `break` to stop once the target is found.

6) Display the search result.
   a) Print the target value.
   b) Print the position where it was found.
   c) Print the number of checks used.

7) Compare best, average, and worst cases.
   a) Use `len(scores) // 2` to estimate the average case.
   b) Show best case as 1 check or `O(1)`.
   c) Show average case as `O(n)`.
   d) Show worst case as 9 checks or `O(n)`.

8) End with the Big-O idea.
   a) Print all three cases together.
   b) Explain that Big-O uses the worst case.
   c) Show that linear search has worst-case time complexity `O(n)`.
"""

# 02-best-average-worst.py

# Topic: Worst, Average and Best Case

# Same list. Steps depend on where the target is.

scores = [3, 7, 2, 9, 4, 1, 8, 5, 6]
# 1 2 3 4 5 6 7 8 9

input("List: " + str(scores) + " n = 9 Linear search — checks left to right. Press Enter ")
target = int(input("Enter a number to search for: "))
input("Searching for " + str(target) + ". Press Enter to run ")

steps = 0

for score in scores:
  steps += 1
  if score == target:

   break

print(" target =", target, " found at position", steps, " checks =", steps)
input("Compare with best and worst case. Press Enter ")
mid = len(scores) // 2
print(" Best: 1 check -> O(1) Average:", mid, "checks -> O(n) Worst: 9 checks -> O(n) Yours:", steps)

input("All three cases. Press Enter ")
print(" Best O(1) Average O(n) Worst O(n) -> Big-O = worst case = O(n).")

          
            