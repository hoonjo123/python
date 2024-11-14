#range
a = range(10)
print(list(a)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a = range(1,10)
print(list(a)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
  print("hello") #hello 10번 출력

for j in range(10):
  print(j) #0부터 9까지 출력

#그렇다면 10,9,8,7....,1과 같이 출력하려면 어떻게 해야할까? 
for k in range(10,1,-1): #-1로 조건 주면 끝!
  print(k)

#while문
i = 1
while i<=10:
  print(i)
  i+=1

i = 10
while i>=1:
  print(i)
  i = i-1

#break
i = 1
while True:
  print(i)
  if i == 10:
    break
  i+=1

#continue
for i in range(1, 11):
  if i%2 == 0:
    continue
  print(i)

#for else
for i in range(1,11):
  print(i)
  if i == 5:
    break
else:
  print(11)
