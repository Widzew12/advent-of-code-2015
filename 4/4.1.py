import hashlib

input_str = input()

i = 0
while True:
    key = (input_str + str(i)).encode()
    key_hash = hashlib.md5(key).hexdigest()
    if key_hash[:5] == "00000":
        print(i)
        break
    i += 1
