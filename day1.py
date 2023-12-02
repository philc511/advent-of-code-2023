with (open('a.txt') as f):
    words = f.readlines()

vals = list(int(next(c for c in w if c.isdigit()) + next(c for c in reversed(w) if c.isdigit())) for w in words)

print(sum(vals))
