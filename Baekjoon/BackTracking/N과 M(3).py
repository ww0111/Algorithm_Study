from itertools import product

N, M = map(int, input().split())

for case in product(range(1, N+1), repeat=M):
    print(*case)
