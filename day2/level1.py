import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from input_loader import InputLoader
import re

lvl1_file = "day2/day2_puzzle_input.txt"
loader = InputLoader(lvl1_file)
input = loader.content

if __name__ == "__main__":
    print("This is level 1")
    if not input:
        raise ValueError("No input exists.")
    
    input_ranges = input.split(',')
    ### ranges with only 3 digits (on both) cannot be accounted for in the invalid IDs
    
    for rng in input_ranges:
        print(rng)
    # print(f"Result: {res}")
