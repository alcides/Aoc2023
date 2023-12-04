

def parse_card(line):
    
    n, relevant = line.split(":")
    n = int(n.split(" ")[-1])
    right, left = relevant.split(" | ")
    
    right = [ int(x.strip()) for x in right.split(" ") if x]
    left = [ int(x.strip()) for x in left.split(" ") if x ]
    return n, right, left

lines = [ parse_card(line) for line in open("input.txt").readlines()]


def matching(right, left):
    return sum([1 for v in left if v in right])
            

storage = {}

for (n, right, left) in lines[::-1]:
    h = matching(right, left)
    count = 1
    if h > 0:
        for i in range(h):
            count += storage[n+i+1]
    storage[n] = count
    
total = sum(storage.values())
print(total)