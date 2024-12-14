with open("5.txt", "r") as input_file:
    input_data = [line.strip() for line in input_file.readlines()]
    
    good_strings_counter = 0
    
    for line in input_data:
        req_1_count = line.count("a") + line.count("e") + line.count("i") + line.count("o") + line.count("u")
        if req_1_count < 3:
            continue
        
        req_2 = False
        for i in range(len(line) - 1):
            if line[i] == line[i+1]:
                req_2 = True
                break
        if not req_2:
            continue
        
        req_3_count = line.count("ab") + line.count("cd") + line.count("pq") + line.count("xy")
        if req_3_count > 0:
            continue
        
        good_strings_counter += 1
    
    print(good_strings_counter)
    