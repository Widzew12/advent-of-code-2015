with open("8.txt", "r") as input_file:
    input_data = [line.strip() for line in input_file.readlines()]
    
    mem_chars_num = 0
    code_chars_num = 0
    for line in input_data:
        code_chars_num += len(line)
        
        new_line = line[1:-1]
        if len(new_line) == 0:
            continue
        
        was_backslash = False
        hex_count = 0
        is_hex = False
        for c in new_line:
            if is_hex:
                if hex_count == 1:
                    is_hex = False
                hex_count += 1
                continue
            elif was_backslash:
                was_backslash = False
                if c in ("\\", '"'):
                    mem_chars_num += 1
                    continue
                elif c == "x":
                    is_hex = True
                    hex_count = 0
                    mem_chars_num += 1
                    continue
            elif c == "\\":
                was_backslash = True
                continue
            mem_chars_num += 1
    
    print(code_chars_num)
    print(mem_chars_num)
    print()
    print(code_chars_num - mem_chars_num)
        