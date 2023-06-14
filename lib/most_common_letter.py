def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) +1
        #print(f"* added key: {char}")
        #print(f"* counter: {counter}")
    # " " is the most common char
    del counter[" "]
    print(f"* Counter: {counter}")
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    print(f"* Sorted items: {counter.items()}")
    print(f"* letter: {letter}")
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")