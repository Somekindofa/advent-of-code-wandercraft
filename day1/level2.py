### This time, we add the zero-crossings, not just the zero-pointings
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from day1.level1 import input_to_signed_numbers
from input_loader import InputLoader

### Let's import the answer from level1
lvl1_answer = 1029
lvl1_file = "lvl1/level1_puzzle_input.txt"
test_file = "lvl2/test_input.txt"
loader = InputLoader(lvl1_file)
input = loader.content
### the intuition would be to watch for the modulo changes. If the acc % 100 != acc then we've crossed the 0 dial

if __name__ == "__main__":
    print("This is level 2")
    if not input:
        raise ValueError("No input exists.")
    
    # we instantiate an accumulator, init at 50
    acc = 50
    # and a counter for the number of zero-crossings, init at 0
    ctr_zc = 0

    # for loop on the list of turns, retrieving the letter to convert to minus or plus
    # and retrieveing the number to accumulate on "acc"
    data_list = input.split()
    signedN = input_to_signed_numbers(data_list)
    for sn in signedN:
        old_acc = acc
        new_pos = old_acc + sn
        new_pos_wrapped = new_pos % 100
        
        # count how many multiples of 100 are encountered during this rotation
        if sn > 0:
            num_zeros = (old_acc + sn) // 100 - old_acc // 100
        elif sn < 0:
            # backward formula (old_acc - 1 means we exclude the starting point)
            num_zeros = (old_acc - 1) // 100 - (old_acc + sn - 1) // 100
        else:
            num_zeros = 0
        
        acc = new_pos_wrapped
        ctr_zc += num_zeros

    print(f"Result: {ctr_zc}")
