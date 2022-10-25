"""

This python file should contain all the helpful functions
that are useful in *all* challenges, e.g. input parsing.

If you add a function, please explain clearly what it does;
what goes in, what comes out. 

"""

from ast import Call
from typing import Callable     # this library handles type hinting for functions

class Puzzle():
    """
    Class to handle the puzzle. 
    
    """
    
    def __init__(self, day_id: str) -> None:
        """
        This 'init' function happens 
        automatically when the class is created.

        Args:
            day_id (str): the day of the challenge.
        """
        
        self.input = self.parse_puzzle_input(day_id)
    

    def parse_puzzle_input(self, day_id:str) -> list:
        """Tom's input parsing code for Advent of Code.

        Args:
            day_id (str): the day of the challenge.

        Returns:
            list: puzzle input as list, one element per line.
        """
        output = []
        with open(f'../data/day_{day_id}_input.txt') as infile:
            output.extend(line.rstrip('\n') for line in infile)
        return output
    
    def read_examples(self, example_tuples: list) -> None:
        
        self.examples = example_tuples

    def verify_solution(self, function: Callable) -> None:
        """Function for verifying that a solution works.

        Args:
            function: python function that solves the problem.
            
            example_tuples (list): list of tuples containing examples.
                                    first element is input, second is output. 
        """
        
        fail = False
        
        for example_input, example_ouput in self.examples:
            
            actual_output = function(example_input)
            
            if actual_output != example_ouput:
                
                print(f"Input: {example_input}\nExpected output: {example_ouput}\nActual output: {actual_output}\n\n")
                
                fail = True
                
        if fail:
            
            print("Solution failed - modify and try again.")
            
        else:
            
            print("Solution passed!")
            
    def show_solution(self, function: Callable):
        
        print(f"The solution is {function(self.input)}.")
                