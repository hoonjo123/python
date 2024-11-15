
#1부터 N까지 홀수 출력하기
n = int(input())
for i in range(1,n+1):
  if i % 2 != 0:
    print(i)

#1부터 N까지의 합 구하기
sum = 0
for j in range(1,n+1):
  sum = sum+j
print(sum) #55

#N의 약수 출력하기
# n = int(input())
for i in range(1, n+1):
  if n % i == 0:
    print(i, end=' ')