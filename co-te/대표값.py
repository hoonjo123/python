

N = int(input())

scores = list(map(int,input().split()))

avg = round(sum(scores)/N)

min_diff = float('inf')
result_score = -1
result_index = -1

for idx, score in enumerate(scores):
  diff = abs(score - avg)


  if diff < min_diff:
    min_diff = diff
    result_score = score
    result_index = idx +1
  
  elif diff == min_diff:
    if score > result_score:
      result_score = score
      result_index = idx +1
    elif score == result_score and idx + 1 < result_index:
      result_index = idx +1


print(avg, result_index)