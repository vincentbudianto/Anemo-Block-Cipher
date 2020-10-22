import json

sbox = []

for i in range(0, 16):
    row = []
    for j in range(0, 16):
        row.append(i*16+j)
    sbox.append(row)

with open("sbox.json", "w") as f:
    json.dump(sbox, f)