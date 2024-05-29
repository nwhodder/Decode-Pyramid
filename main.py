def decode(message_file: str):
    words_map = {}  # Create dictionary that we will map the integers and words to
    with open(message_file, "r") as f:
        for line in f:
            sepearated = line.split(" ")    # Separate ints from strings in each line
            words_map.update({int(sepearated[0]): sepearated[1].strip()})   # Update words_map with separated key/value pairs
    words_map = dict(sorted(words_map.items())) # sort words_map by key (int)
    pyramid = createPyramid(words_map)
    for i in range(len(pyramid)):   # For each list in pyramid, return the last value from it and the associated word
        print(f"{pyramid[i][-1]}: {words_map[pyramid[i][-1]]}")

def createPyramid(d: dict):
    pyramid = []    # List of lists for pyramid
    temp_list = []  # List for editing and appending to pyramid list
    num = 1     # Value to keep track of required list length
    for i in d:
        temp_list.append(i) # Append to temp_list
        if len(temp_list) == num :  # If temp_list is the right length append it to pyramid list and reset it,
            pyramid.append(temp_list)   # increasing list length requirement by 1
            num += 1
            temp_list = []
    return pyramid
        
decode("coding_qual_input.txt")
