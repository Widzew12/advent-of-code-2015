wire_dict = dict()
circuit_dict = dict()

def get_wire(target):
    if target in wire_dict:
        return wire_dict[target]
    
    circuit = circuit_dict[target]
    operation = circuit[0]
    
    output = None
    
    if operation in (0, 1):
        wire = circuit[1]
        if wire.isnumeric():
            wire = int(wire)
        else:
            wire = get_wire(wire)
        
        if operation == 0:
            output = wire
        elif operation == 1:
            output = ~wire
    elif operation in (2, 3, 4, 5):
        wire_1 = circuit[1]
        wire_2 = circuit[2]
        
        if wire_1.isnumeric():
            wire_1 = int(wire_1)
        else:
            wire_1 = get_wire(wire_1)
        
        if wire_2.isnumeric():
            wire_2 = int(wire_2)
        else:
            wire_2 = get_wire(wire_2)
        
        if operation == 2:
            output = wire_1 & wire_2
        elif operation == 3:
            output = wire_1 | wire_2
        elif operation == 4:
            output = wire_1 << wire_2
        elif operation == 5:
            output = wire_1 >> wire_2

    wire_dict[target] = output
    return output

with open("7.txt", "r") as input_file:
    input_data = [line.strip() for line in input_file.readlines()]
    
    operations = {"NONE": 0,
                  "NOT": 1,
                  "AND": 2,
                  "OR": 3,
                  "LSHIFT": 4,
                  "RSHIFT": 5}
    
    for line in input_data:
        split_line = line.split(" ")
        target = split_line[-1]
        if len(split_line) == 3:
            circuit_dict[target] = (0, split_line[0])
        elif len(split_line) == 4:
            circuit_dict[target] = (1, split_line[1])
        elif len(split_line) == 5:
            operation = split_line[1]
            circuit_dict[target] = (operations[operation], split_line[0], split_line[2])
    
    wire_a = get_wire("a")
    
    circuit_dict["b"] = (0, str(wire_a))
    wire_dict = dict()
    
    wire_a = get_wire("a")
    
    print()
    print(wire_a)
    