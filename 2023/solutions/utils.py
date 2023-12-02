"""
Helpful classes and functions to aid with advent of code solving. 
"""

def load_puzzle_input(day: int):
    """
    Loads the puzzle input for the date in December (int).
    """
    
    with open(f"../data/day_{day:02}.txt", 'r') as infile: 
    
        return infile.read().splitlines()
    
def load_example_input(day: int, part: int):
    """
    Loads the puzzle example for the date in December (int) and the puzzle part.
    """
    
    with open(f"../examples/day_{day:02}_part_{part}.txt", 'r') as infile: 
    
        return infile.read().splitlines()
    
def test_code(func, example_dict, debug = False):
    """
    Tests the solver function against the known examples.
    
    Arguments: 
        func: solution function
        example dict: dictionary with format {example_input: example_solution}
    """
    
    failed = False

    for sample_index, (sample_input, sample_output) in enumerate(example_dict.items()):

        if debug:
            print(f'sample_input: {sample_input}')
            print(f'sample_output: {sample_output}')
        
        if func(sample_input) == sample_output:
            
            print(f"Test {sample_index} passed: Input <{sample_input}> gives output <{sample_output}>.")
            
        else:
            
            print(f"Test {sample_index} failed: Input <{sample_input}> expected <{sample_output}>, but got <{func(sample_input)}>.")
            failed = True

    print()
    if failed: 
        print("Didn't get it this time... Try again! You got this!")
    else:
        print("Congratulations! Looks like you cracked it! Good job!")     