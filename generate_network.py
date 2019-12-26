from os import linesep as nl

def decipher(n):
    a, b, c, d, e = [int(x) for x in f"{n:05b}"]
    p = (1^c) & (a|b)^(1^d)
    q = a & b & (1^c) & (1^d) ^ d & e & (a | (1^c))
    r = 1^e & (b|c|d)
    s = (a^e) & (b^c^d & e)
    t = (1^b) ^ e ^ (d & (c | e))
    return int(''.join(['01'[i] for i in [p,q,r,s,t]]), 2)

with open("network.csv", "w") as f:
    lines = [f"{i},{decipher(i)}{nl}" for i in range(32)]
    f.write(''.join(lines))
