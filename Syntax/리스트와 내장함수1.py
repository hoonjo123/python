a = [23, 12, 36, 53, 19]
print(a[:3]) #[23, 12, 36] 0부터 2번 인덱스까지

print(len(a)) #5

#list 출력해보기
for i in range(len(a)):
  print(a[i],end=' ')
print()

for x in a:
  print(x,end=' ')
print()

for j in a:
  if j % 2 == 0:
    print(j, end=" ") #12, 36
print()

for k in enumerate(a):
  print(k, end=" ") #(0, 23) (1, 12) (2, 36) (3, 53) (4, 19) 튜플형태로 출력
print()

#튜플
b = (1,2,3,4,5)
print(b[0]) #1
# b[0] = 7 순서가 정해져있지 않기 때문에 에러가 난다.


#튜플접근
for x in enumerate(a):
  print(x[0], x[1],end=" ") #0 23 1 12 2 36 3 53 4 19
print()

for index,value in enumerate(a):
  print(index, value, end=" ") #0 23 1 12 2 36 3 53 4 19
print()

#all과 any
if all(60>x for x in a):
  print("YES")
else:
  print("NO") #YES


if any(15>x for x in a): #한번이라도 x값중에 참이 있다면 YES
  print("YES")
else:
  print("NO") #YES

