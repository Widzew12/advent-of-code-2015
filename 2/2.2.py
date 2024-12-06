with open("2.txt", "r") as input_file:
    data = [sorted([int(num) for num in line.strip().split("x")]) for line in input_file.readlines()]
    total_num = 0
    for box in data:
        total_num += 2 * box[0] + 2 * box[1] + box[0] * box[1] * box[2]
    print(total_num)