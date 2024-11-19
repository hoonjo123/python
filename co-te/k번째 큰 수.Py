from itertools import combinations

n, k = map(int,input().split())

cards = list(map(int,input().split()))

sums = set(sum(i) for i in combinations(cards,3))
sorted_sums = sorted(sums,reverse=True)
print(sorted_sums[k-1])