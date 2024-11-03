import json
import pytest
from itertools import product
from priority import *

def apply(actions:list[int|None], cls) -> list[int]:
    tool = cls()
    max_numbers = []
    for item in actions:
        if item is None:
            max_numbers.append(tool.pop_max())
        else:
            tool.push(item)
    return max_numbers

TOOLS = [ LazyPriorityList, PriorityList, PriorityDequeue, PriorityQueue ]
SIZES = [ 10, 100, 1000, 10000, 100000 ] 

@pytest.mark.parametrize("size, tool", product(SIZES,TOOLS))
def test_all(size,tool): 
    with open(f"Random_cases_{size}.json") as f:
        tests = json.load(f)    
    for testcase in tests:
        assert testcase["output"] == apply(testcase["input"],tool)                
                    
                    

