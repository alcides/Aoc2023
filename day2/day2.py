sum = 0

maximums = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def parse_play(p:str):
    number, color = p.strip().split(" ")
    return number, color

for line in open("i2.txt"):
    d, r = line.split(":")
    games = [ [ parse_play(p) for p in game.split(",")] for game in r.split(";")]
    gid = int(d.split(" ")[-1])
    
    exceeds = any([any([ int(n) > maximums[c] for n, c in g ]) for g in games])
    if not exceeds:
        sum += gid
                
print(sum)

    
    