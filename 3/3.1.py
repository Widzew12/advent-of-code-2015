with open("D:\\Programowanie\\Advent of code\\advent-of-code-2015\\3\\3.txt", "r") as input_file:
    data = input_file.readline().strip()
    index = (0, 0)
    index_dict = {index: 1}
    for ch in data:
        if ch == "^":
            index = (index[0] - 1, index[1])
        elif ch == "v":
            index = (index[0] + 1, index[1])
        elif ch == "<":
            index = (index[0], index[1] - 1)
        elif ch == ">":
            index = (index[0], index[1] + 1)
        if index in index_dict:
            index_dict[index] += 1
        else:
            index_dict[index] = 1
    
    number = 0
    for val in index_dict.values():
        number += 1 if val >= 1 else 0

    print(number)
    