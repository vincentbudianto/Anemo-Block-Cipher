import random

# arr = bytearray of plaintext
# key = bytearray of key, size = 64 bytes
# sbox = sbox matrix of 16*16
def encrypt(arr, key, sbox):
    res = []
    prevBlock = [0, 0, 0, 0, 0, 0, 0, 0] # default previous block
    newData = []
    # For every block in data
    for i in range(0, len(arr), 8):
        # Sets random seed
        random.seed(prevBlock[0])
        roundkeys=[]
        indexes = []
        index = []
        for j in range(0, 4):
            index.append(random.randint(0,len(key)-1))
        indexes.append(index)
        roundkeys.append([key[index[0]], key[index[1]], key[index[2]], key[index[3]]])
        # Gets how many rounds
        rounds = (roundkeys[0][0] % 16) + 1
        # Splits block in two
        leftBlock = arr[i : i+4]
        rightBlock = arr[i+4 : i+8]
        # Gets byte indexes for round keys
        for i in range(0, rounds):
            index = []
            for j in range(0, 4):
                index.append(random.randint(0,len(key)-1))
            indexes.append(index)
            roundkey = [key[index[0]], key[index[1]], key[index[2]], key[index[3]]]
            roundkeys.append(key)
            XORright = []
            newLeft = []
            for i in range(0,4):
                XORright.append(rightBlock[i]^roundkey[i])
            for i in range(0,4):
                newLeft.append(XORright[i]^leftBlock[i])
            leftBlock = rightBlock
            rightBlock = newLeft
        prevBlock = leftBlock + rightBlock
        newData += prevBlock

            
        print(rounds)
        print(prevBlock)
    print(len(arr))
    print(len(newData))

