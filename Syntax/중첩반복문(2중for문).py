
#2중 for문
"""
for i in range(5):
  print("i :", i,sep=' ',end=' ')
  for j in range(5):
    print("j :", i,sep=' ',end=' ')
"""
#별찍어보기
"""
for i in range(5):
  for j in range(5):
    print("*",end=' ')
  print()
"""

#별찍어보기1
for i in range(5):
  for j in range(i+1):
    print("*",end=' ')
  print()

#별찍어보기2
for i in range(5):
  for j in range(5-i):
    print("*",end=' ')
  print()


