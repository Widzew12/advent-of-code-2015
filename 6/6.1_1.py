SIZE = 1000

with open("6.txt", "r") as input_file:
    input_data = [line.strip() for line in input_file.readlines()]
    
    grid = [[False for _ in range(SIZE)] for _ in range(SIZE)]
    
    for line in input_data:
        if "turn on" in line:
            start_pos_str, _, end_pos_str = line[8:].split(" ")
        elif "turn off" in line:
            start_pos_str, _, end_pos_str = line[9:].split(" ")
        elif "toggle" in line:
            start_pos_str, _, end_pos_str = line[7:].split(" ")
        
        start_pos_x, start_pos_y = (int(element) for element in start_pos_str.split(","))
        start_pos = (start_pos_x, start_pos_y)
        end_pos_x, end_pos_y = (int(element) for element in end_pos_str.split(","))
        end_pos = (end_pos_x, end_pos_y)
        
        print(start_pos, end_pos)
        
        for x in range(start_pos_x, end_pos_x + 1):
            for y in range(start_pos_y, end_pos_y + 1):
                if "turn on" in line:
                    grid[x][y] = True
                elif "turn off" in line:
                    grid[x][y] = False
                elif "toggle" in line:
                    grid[x][y] = not grid[x][y]
        
    lit_lights = 0
    for line in grid:
        lit_lights += line.count(True)
    
    print(lit_lights)
    