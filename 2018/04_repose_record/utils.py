def load_puzzle_input():
    
    with open('input.txt', 'r') as infile: 
    
        return infile.read().splitlines()
    
def test_code(func, example_dict):
    
    failed = False
    
    for sample_index, (sample_input, sample_output) in enumerate(example_dict.items()):
        
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