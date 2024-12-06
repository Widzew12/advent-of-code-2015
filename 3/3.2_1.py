with open("D:\\Programowanie\\Advent of code\\advent-of-code-2015\\3\\3.txt", "r") as input_file:
    data = input_file.readline().strip()
    curr_index = [(0, 0), (0, 0)]
    index_dict = {(0, 0): 1}
    for i in range(len(data)):
        curr_index[1 if i % 2 else 0] = (curr_index[1 if i % 2 else 0][0] - 1, curr_index[1 if i % 2 else 0][1]) if data[i] == "^" else (curr_index[1 if i % 2 else 0][0] + 1, curr_index[1 if i % 2 else 0][1]) if data[i] == "v" else (curr_index[1 if i % 2 else 0][0], curr_index[1 if i % 2 else 0][1] - 1) if data[i] == "<" else (curr_index[1 if i % 2 else 0][0], curr_index[1 if i % 2 else 0][1] + 1) if data[i] == ">" else ""
        index_dict[curr_index[1 if i % 2 else 0]] = 1 if curr_index[1 if i % 2 else 0] not in index_dict else index_dict[curr_index[1 if i % 2 else 0]] + 1
    num = sum([1 if val >= 1 else 0 for val in index_dict.values()])
    print(num)
    