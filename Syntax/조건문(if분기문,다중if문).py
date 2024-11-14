x = 7
if x == 7: #관계연산자, 같지않을경우 !=
  print("Lucky")
  print("smash")

else:
  print("Bad")


x = 15
if x>=10:
  if x%2==1:#홀수
    print("10이상의 홀수") #10이상의 홀수


x = 9
if x>0:
  if x<10:
    print("10보다 작은 자연수")
  else:
    print("10보다 큰것같아요")

#한 줄로 작성해보자
x = 7
if x>0 and x<10:
  print("10보다 작은 자연수")

#and연산 없이 
if 0<x<10: #C나 C++등 다른 언어는 불가한 부분
  print("10보다 작은 자연수")



x = 10
if x>0:
  print("양수")
else:
  print("음수")

#다중if문
x = 93
if x>=90:
  print('A')
elif x>=80:
  print('B')
elif x>=70:
  print('C')
elif x>=60:
  print('D')
else:
  print("F")