with open("1.txt", "r") as input_file:
    i = 0
    input_data = input_file.read().strip()
    for j in range(len(input_data)):
        if input_data[j] == "(":
            i += 1
        elif input_data[j] == ")":
            i -= 1
        if i < 0:
            print(j+1)
            break
