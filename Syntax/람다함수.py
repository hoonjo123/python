def plus_one(x):
  return x + 1

print(plus_one(1)) # 2

#람다함수
plus_two = lambda x: x+2
print(plus_two(1)) # 3


a = [1,2,3]
print(list(map(plus_one, a))) #[2,3,4]
print(list(map(lambda x: x+1, a))) #[2,3,4] 맵이라는 함수에 인자를 받아 한번에! 정말편리하다 우와
