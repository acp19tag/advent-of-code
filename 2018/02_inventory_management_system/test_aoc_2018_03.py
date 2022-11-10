import pathlib
import pytest

#################
# CHANGE [XX] TO DAY
import aoc_2018_03 as aoc 
#################

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():

    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():

    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

#################

#################
def test_parse_example1(example1):

    """Test that input is parsed properly"""

    #################
    # ADD EXAMPLE 1 PARSED FORM HERE
    assert example1 == [
        (1, 1, 3, 4, 4),
        (2, 3, 1, 4, 4),
        (3, 5, 5, 2, 2)
    ] 
    #################
    
#################
# DELETE WHEN USED
@pytest.mark.skip(reason="Not implemented") 
#################
def test_part1_example1(example1):

    """Test part 1 on example input"""

    #################
    # ADD EXAMPLE 1 SOLUTION HERE
    assert aoc.part1(example1) == 4
    #################


#################
# DELETE WHEN USED
@pytest.mark.skip(reason="Not implemented") 
#################
def test_part2_example2(example2):

    """Test part 2 on example input"""

    #################
    # ADD EXAMPLE 2 SOLUTION HERE
    assert aoc.part2(example2) == ...
    #################
