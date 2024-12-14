SIZE = 1000

with open("6.txt", "r") as input_file:
    input_data = [line.strip() for line in input_file.readlines()]
    
    grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    
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

        # faster solution
        if "turn on" in line:
            for x in range(start_pos_x, end_pos_x + 1):
                for y in range(start_pos_y, end_pos_y + 1):
                    grid[x][y] += 1
        elif "turn off" in line:
            for x in range(start_pos_x, end_pos_x + 1):
                for y in range(start_pos_y, end_pos_y + 1):
                    grid[x][y] = max(grid[x][y] - 1, 0)
        elif "toggle" in line:
            for x in range(start_pos_x, end_pos_x + 1):
                for y in range(start_pos_y, end_pos_y + 1):
                    grid[x][y] += 2
        
    total_brightness = 0
    for line in grid:
        total_brightness += sum(line)
    
    print(total_brightness)
    