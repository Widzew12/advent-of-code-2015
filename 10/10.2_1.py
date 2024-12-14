curr_str = "1113222113"

state = [(3, 1), (1, 3), (3, 2), (2, 1), (1, 3)]

for i in range(49):
    new_state = []

    for e1, e2 in state:
        new_state.append(e1)
        new_state.append(e2)

    state = []
    curr_num = 0
    counter = 0
    for element in new_state:
        if curr_num == element:
            counter += 1
            continue

        if counter > 0:
            new_element = (counter, curr_num)
            state.append(new_element)
        
        counter = 1
        curr_num = element

    new_element = (counter, curr_num)
    state.append(new_element)

    print(i)
    print(len(state)*2)
