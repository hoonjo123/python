N = int(input())
a = list(map(int,input().split()))

def digit_sum(x):
  sum = 0
  while x>0:
    sum+= x%10
    x=x//10
  return sum
  
max = 0
for x in a:
  total = digit_sum(x)
  if total>max:
    max = total
    res = x
print(res)