curr_str = "1113222113"
#curr_str = "1"

def get_num(curr_str):
    for i in range(10):
        new_str = ""
        counter = 1
        prev_c = ""
        for c in curr_str:
            if c == prev_c:
                counter += 1
            else:
                if prev_c != "":
                    new_str += str(counter) + prev_c
                counter = 1
            prev_c = c
        new_str += str(counter) + prev_c
        curr_str = new_str
        print(i)
    return len(curr_str)

def get_index(curr_str, start_index):
    curr_c = curr_str[0]
    i = start_index
    while i < len(curr_str):
        if curr_str[i] != curr_c:
            return i
        i += 1
    
    
for i in range(40):
    new_str = ""
    counter = 1
    prev_c = ""
    for c in curr_str:
        if c == prev_c:
            counter += 1
        else:
            if prev_c != "":
                new_str += str(counter) + prev_c
            counter = 1
        prev_c = c
    new_str += str(counter) + prev_c
    curr_str = new_str
    print(i)

str_len = len(curr_str)

s_index_1 = 0
s_index_2 = get_index(curr_str, str_len // 4)
s_index_3 = get_index(curr_str, str_len // 2)
s_index_4 = get_index(curr_str, 3 * str_len // 4)

curr_str_1 = curr_str[:s_index_2]
curr_str_2 = curr_str[s_index_2:s_index_3]
curr_str_3 = curr_str[s_index_3:s_index_4]
curr_str_4 = curr_str[s_index_4:str_len]

len_1 = get_num(curr_str_1)
len_2 = get_num(curr_str_2)
len_3 = get_num(curr_str_3)
len_4 = get_num(curr_str_4)


print(len_1 + len_2 + len_3 + len_4)
    