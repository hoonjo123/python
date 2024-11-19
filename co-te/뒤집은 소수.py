def reverse(x):
  return int(str(x)[::-1])

def isPrime(x):
  if x==1:
    return False
  for i in range(2, int(x**0.5) + 1):
    if x%i == 0:
      return False
  else:
    return True

n = int(input())
a = list(map(int,input().split()))

for x in a:
  tmp = reverse(x)
  if isPrime(tmp):
    print(tmp,end=' ')