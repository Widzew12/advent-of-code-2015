with open("8.txt", "r") as input_file:
    input_data = [line.strip() for line in input_file.readlines()]
    
    code_chars_num = 0
    
    new_chars_num = 0
    
    for line in input_data:
        code_chars_num += len(line)
        new_line = line[1:-1]
        chars_num = 6
        
        for c in new_line:
            chars_num += 1
            if c in ("\\", "\""):
                chars_num += 1
            
        new_chars_num += chars_num
    
    print(code_chars_num)
    print(new_chars_num)
    print()
    print(new_chars_num - code_chars_num)
        