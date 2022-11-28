#baekjoon 2839
n = int(input())

bags = [-1 for i in range(max(6, n+1))]

bags[3] = 1
bags[5] = 1

for i in range(6, n+1):
    if bags[i-3] != -1 or bags[i-5] != -1:
        if bags[i-3] != -1 and bags[i-5] != -1:
            bags[i] = min(bags[i-3], bags[i-5]) + 1
        else:
            bags[i] = max(bags[i-3], bags[i-5]) + 1

print(bags[n])