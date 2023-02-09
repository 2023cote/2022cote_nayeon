from itertools import product

candidates = product(product([0, 1], repeat=3), repeat=2)
for c in candidates:
    print(c[0][0])