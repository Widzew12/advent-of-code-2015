curr_str = "1113222113"
#curr_str = "1"

for i in range(50):
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
    print(len(curr_str))

print(len(curr_str))
