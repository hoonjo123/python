import random as r


#리스트 만들기
a = []
print(a)
b = list()
print(b)

a=[1,2,3,4,5]
print(a)
print(a[0]) #1

b = list(range(1,11))
print(b) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c = a + b
print(c) #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a.append(6)
print(a) #[1, 2, 3, 4, 5, 6]

a.insert(3,7)
print(a) #[1, 2, 3, 7, 4, 5, 6] 3번 인덱스로 7삽입

a.pop()
print(a) # 6

a.pop(3)
print(a) #3번 인덱스 제거

a.remove(4) #4제거
print(a)

print(a.index(5)) #3 5라는 값이 몇번 인덱스에 있습니까

#리스트 초기화
a = list(range(1,11))

print(sum(a)) #55
print(max(a)) #10
print(min(a)) #1
print(min(7,5)) #인자가 들어갈경우 최소값을 찾아줍니다.

#셔플 사용하기
r.shuffle(a)
print(a) #랜덤으로 리스트 안에 있는 값을 섞어줍니다. 
a.sort()
print(a) #오름차순으로 다시 정렬
a.sort(reverse=True)
print(a) #내림차순으로 다시 정렬

a.clear() #리스트 값 제거
print(a)