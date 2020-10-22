import json
import random

data = []

for i in range(0, random.randint(10, 100)*8):
    data.append(random.randint(0,255))
    

with open("data.json", "w") as f:
    json.dump(data, f)