# Goal
The goal of this homework is to ensure familiarity with variable and function declaration, as well as using if-else, loops, and try-except statments.

# Instructions for Setup and Execution
1. Install pip and pipenv.  The former allows you to install packages,the second creates what is known as a virtual environment which allows you to download packages without risking impact to your computer.
2. Run `pipenv run pytest path_to_tests/tests.py`
3. You should see test failures, including an explanation of those failures.  In homework.py, follow Instructions for Implementation (below in this document) to implement the functions to pass the all of the tests.


# Instructions for Implementation
1. In the function first_func, there's a list composed of variables.  For now, don't worry about what a list is, just know that the items in the square brackets are variable names, but the values haven't been defined. Define the variables specified in the list to have values of "Hi", 5, 3.14, and True respectively.
2. Define second_func to return 0 if the number a passed in is even, 1 if a is 1, and 2 if it's anything that's not even or 1.
3. For third_func, the type of a and b aren't specified.  Try returning a+b, but catch an error and return the error and only the error.
4. For fourth_func, do string concatenation (result += another_string, where another_string is another string) such that you add "Hi" to the result string the same number of times as a.  For example, if a is 3, return "HiHiHi". 
5.  Finally, write a function called fifth_func that takes in three numbers and returns their product.