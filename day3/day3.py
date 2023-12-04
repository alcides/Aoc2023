from lark import Lark, Token, Tree

grammar = '''
%import common.INT

start: line+
line: (INT | symbol | dot)+ "\\n"
dot: "."
symbol: Q | P | D | S | A | M | V | T | E | R | N
Q: "?"
P: "#"
D: "$"
S: "*"
A: "+"
M: "&"
V: "/"
T: "@"
E: "="
R: "%"
N: "-"
'''
p = Lark(grammar, parser='lalr')


content = open("input3  .txt").read()
start = p.parse(content)


def parse_c(start):
    for c in start.children:
        for p in c.children:
            if isinstance(p, Token):
                if p.type == "INT":
                    yield ("number", p.value, p.line, p.column, p.end_column)
            elif isinstance(p, Tree):
                if p.data == "dot":
                    pass
                elif p.data == "symbol":
                    t : Token = p.children[0]
                    yield ("symbol", t.value, t.line, t.column, t.end_column)
                else:
                    print(f"Could not parse {p.data}, {p.type}")

lines = list(parse_c(start))

symbols = [ x for x in lines if x[0] == 'symbol' ]
numbers = [ x for x in lines if x[0] == 'number' ]

def close(n, s):
    y = n[2]
    ty = s[2]
    tx = s[3]
    for x in range(n[3], n[4]):
        if abs(tx - x) <= 1 and abs(ty - y) <= 1:
            return True
    return False
    

def near(n):
    for s in symbols:
        if close(n, s):
            return True
    return False

target = [ n for n in numbers if near(n) ]
print(sum(int(x[1]) for x in target))