with open("D:\\Programowanie\\Advent of code\\advent-of-code-2015\\3\\3.txt", "r") as input_file:
    data = input_file.readline().strip()
    
    santa_index = (0, 0)
    robo_index = (0, 0)
    index_dict = {(0, 0): 1}
    
    santas_turn = True
    
    for ch in data:
        index = santa_index if santas_turn else robo_index
        
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
        
        if santas_turn:
            santa_index = index
        else:
            robo_index = index
        
        santas_turn = not santas_turn
    
    number = 0
    for val in index_dict.values():
        if val >= 1:
            number += 1

    print(number)
    