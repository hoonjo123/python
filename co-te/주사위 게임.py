N = int(input())
res = 0
for i in range(N):
  tmp = input().split()
  tmp.sort() #3번째 규칙을 보면 가장 큰 숫자를 찾아야하므로 미리 정렬해주기
  a, b, c = map(int,tmp)
  if a==b and b==c:
    money = 10000 +a*1000
  elif a==b or a==c:
    money = 1000+(a*100)
  elif b ==c:
    money = 1000+(b*100)
  else:
    money=c*100

  if money>res:
    res = money
print(res)