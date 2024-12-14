from itertools import permutations

with open("9.txt", "r") as input_file:
    input_data = [line.strip() for line in input_file.readlines()]
    
    distances_dict = dict()
    destinations_set = set()
    
    for line in input_data:
        split_line = line.split(" = ")
        destination_1, destination_2 = split_line[0].split(" to ")
        distance = split_line[1]
        
        if destination_1 not in distances_dict:
            distances_dict[destination_1] = dict()
        distances_dict[destination_1][destination_2] = int(distance)
        
        if destination_2 not in distances_dict:
            distances_dict[destination_2] = dict()
        distances_dict[destination_2][destination_1] = int(distance)
        
        destinations_set.add(destination_1)
        destinations_set.add(destination_2)
    
    destinations_list = list(destinations_set)
    destinations_permutations = list(permutations(destinations_list))
    
    min_distance = 10000000000000
    for permutation in destinations_permutations:
        prev_destination = None
        distance = 0
        for destination in permutation:
            if prev_destination is not None:
                distance += distances_dict[prev_destination][destination]
            prev_destination = destination
        
        min_distance = min(distance, min_distance)
        
    print(min_distance)
