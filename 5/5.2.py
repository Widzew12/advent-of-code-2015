with open("5.txt", "r") as input_file:
    input_data = [line.strip() for line in input_file.readlines()]
    
    good_strings_counter = 0
    
    for line in input_data:
        req_1 = False
        for i in range(len(line) - 1):
            target = line[i:i+2]
            for j in range(len(line) - 1):
                if line[j:j+2] == target and j not in (i - 1, i, i + 1):
                    req_1 = True
                    break
            if req_1:
                break
        if not req_1:
            continue
        
        req_2 = False
        for i in range(len(line) - 2):
            if line[i] == line[i+2]:
                req_2 = True
                break
        if not req_2:
            continue
        
        good_strings_counter += 1
    
    print(good_strings_counter)
    