a = input()
print(a)

a = input("숫자를 입력하세요: ") #숫자를 입력하세요: 3
print(a) #3

a, b  = input("숫자를 입력하세요: ").split()
print(a,b) #2 3
print(a+b) #23 string type
c = a+b
print(type(c))
print(c) #23

a, b = map(int, input().split()) #int type
print(a+b) # 2+3 = 5
print(a//b) #5//2 = 2
print(a%b) #5%2 = 1
print(a**b) #a를 b로 거듭제곱


a = 4.3
b = 5
c = a+b
print(type(c)) #실수 + 정수 => 실수형 9.3

