with open("1.txt", "r") as input_file:
    i = 0    
    for c in input_file.read():
        if c == "(":
            i += 1
        elif c == ")":
            i -= 1
    print(i)