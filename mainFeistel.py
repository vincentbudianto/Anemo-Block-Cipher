import json
import feistel

sbox = []
data = []
key = [104, 101, 108, 108, 111, 32, 72, 45, 65, 45, 66, 98, 42, 7, 70, 107, 41, 75, 97, 102, 32, 75, 98, 41, 72, 46, 14, 69, 39, 14, 70, 104, 102, 35, 4, 10, 76, 36, 66, 97, 101, 111, 35, 7, 69, 36, 65, 46, 13, 10, 79, 107, 42, 4, 9, 3, 76, 39, 13, 9, 0, 3, 79, 104]

with open("sbox.json", 'r') as f:
    sbox = json.load(f)

with open("data.json", 'r') as f:
    data = json.load(f)

feistel.encrypt(data, key, sbox)