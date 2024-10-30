import cProfile
import searcher
import time

def slow_function():
    time.sleep(5)

def main():
    searcher.linear_search([1,2,3], 5)
    slow_function()

cProfile.run("main()")