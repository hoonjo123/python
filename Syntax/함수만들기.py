#기본 함수의 구조
def add(a, b):
  c = a+b
  print(c)

add(3,2)
add(5,7)

#1
def add(a, b):
  c = a+b
  return c #return 은 값을 꺼내고 함수를 종료하는 역할 
x = add(3,2)
print(x) #5

#2
def add(a,b):
  c = a+b
  d = a-b
  return c, d

x = add(3,2)
print(x) #(5,1) 튜플자료형으로 리턴



#3 소수만 출력해보기
def isPrime(x):
  for i in range(2, x):
    if x % i ==0: #약수가 있다면? false로 함수 종료
      return False
  return True

a = [12, 13, 7, 9, 19]
for x in a:
  if isPrime(x):
    print(x, end=" ") #13 7 19