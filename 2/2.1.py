with open("2.txt", "r") as input_file:
    data = [[int(num) for num in line.strip().split("x")] for line in input_file.readlines()]
    total_num = 0
    for box in data:
        area1 = box[0] * box[1]
        area2 = box[1] * box[2]
        area3 = box[0] * box[2]
        total_num += 2 * area1 + 2 * area2 + 2 * area3 + min(area1, area2, area3)
    print(total_num)