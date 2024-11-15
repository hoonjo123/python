a = [0]*3
print(a) #[0, 0, 0] 1차원 리스트

#2차원 리스트 생성하기

a = [[0]*3 for _ in range(3)]
print(a) 
#[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

a[0][1] = 1
print(a) 
#[[0, 1, 0], [0, 0, 0], [0, 0, 0]]

for i in a:
  print(i) 
#[0, 1, 0]
#[0, 0, 0]
#[0, 0, 0]
  
for x in a:
  for y in x:
    print(y,end=' ')
  print()

"""
0 1 0 
0 0 0 
0 0 0
"""