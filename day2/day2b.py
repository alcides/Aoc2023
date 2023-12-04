sum = 0


def parse_play(p:str):
    number, color = p.strip().split(" ")
    return int(number), color

for line in open("i2.txt"):
    d, r = line.split(":")
    games = [ [ parse_play(p) for p in game.split(",")] for game in r.split(";")]
    gid = int(d.split(" ")[-1])
    
    minimums = {"green": 0, "blue": 0, "red":0}
    for g in games:
        for n, c in g:
            minimums[c] = max(n, minimums[c])
    
    power = minimums["green"] * minimums["red"] * minimums["blue"]
    sum += power
                
print(sum)

    
    