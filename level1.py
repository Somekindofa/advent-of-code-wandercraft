from input_loader import InputLoader
import re

lvl1_file = "level1_puzzle_input.txt"
loader = InputLoader(lvl1_file)
input = loader.content

if __name__ == "__main__":
    print("This is level 1")
    if not input:
        raise ValueError("No input exists.")
    
    # we instantiate an accumulator, init at 50
    acc = 50
    # and a counter for the number of zero crossings, init at 0
    ctr = 0

    # for loop on the list of turns, retrieving the letter to convert to minus or plus
    # and retrieveing the number to accumulate on "acc"
    data_list = input.split()

    def input_to_signed_numbers(input: list[str]):
        signs = [1 if re.search(r"R", i) else -1 for i in input]
        numbers = [int(re.search(r"\d+", i).group()) for i in input]
        signed_numbers = [s * n for s, n in zip(signs, numbers)]  
        return signed_numbers

    signedN = input_to_signed_numbers(data_list)
    for sn in signedN:
        acc += sn
        acc = acc % 100
        if acc == 0:
            ctr += 1
    
    print(f"Result: {ctr}")
