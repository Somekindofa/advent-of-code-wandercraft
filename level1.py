from input_loader import InputLoader

lvl1_file = "level1_puzzle_input.txt"
loader = InputLoader(lvl1_file)
data = loader.content

if __name__ == "__main__":
    print("This is level 1")
    if data:
        print(f"Loaded data length: {len(data)}")