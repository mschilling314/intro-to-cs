# Goal
The goal of this assignment is to ensure familiarity with the basic data structures in Python.

# Setup
1. Run `pipenv run pytest path_to_tests/tests.py`
2. You should see test failures, including an explanation of those failures.  In homework.py, follow Instructions for Implementation (below in this document) to implement the functions to pass the all of the tests.


# Instructions for Implementation
## Lists
1. Define a list with the integers 1, 3, 5, 7, 9.  Bonus points if you can do this by constructing it using a for loop and range, extra bonus points if you look up list comprehension.
2. Given a list of ints, return a list of even ints.  Bonus points if you do this using list comprehension.
3. We're now going to implement a famous algorithm: binary search.  The premise is simple, I will give you a sorted list, and a target number, you'll tell me if the target number is in the sorted list.  If it is, you'll return the index you find the number at, if it's not, return -1. Your algorithm should run in O(logn). Solve without using any imports first, then if you're curious, look up bisect.

## Dicts
1. Create a dictionary such that if I use the keys "dog", "cat", and "duck" respectively I get "bark", "meow", and "quack" back.
2. Given a dict, tell me if a key-value pair is present in the dict.

## Bonus
For the bonus question, we invite you to solve the following problem.  You will be given a list of numbers, and a target.  Return true if and only if two distinct numbers in the list add up to the target, otherwise return false.

### Example
list_ints = [2, 1, 4, 3]
target = 7

We'd expect to return true, because 4+3 is 7.

### Example
list_ints = [2, 1, 4, 3]
target = 2

We'd expect to return false, because no two numbers will add up to 2, in fact the lowest sum you can get is 3.

### Bonus bonus
Try to come up with a few different ways to solve the problem.  The obvious solution is O(n^2), but there are solutions in O(nlogn), and even O(n).  What are the trade-offs to these solutions? (Hint: space)