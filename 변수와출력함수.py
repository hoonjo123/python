#변수

# ````
# 변수명 정하기
# 1. 영문과 숫자, _ 로 이루어진다.
# 2. 대소문자를 구분한다.
# 3. 문자나 _로 시작한다
# 4. 특수문자를 사용하면 안된다.
# 5. 키워드를 사용하면 안된다.
# ````

#변수 출력하기
a = 1
A = 2
c = 3
print(a, A, c)
A1 = 1

a, b, c = 3, 2, 1
print(a, b, c)

#값교환하기
a, b = 10, 20
print(a,b) #10, 20
a, b = b, a
print(a,b) #20,10

#변수타입
a = 12345
print(type(a)) #int

a = 12.1234
print(type(a)) #float
a = 'student'
print(type(a)) #String

#출력방식
print("number")
a, b, c = 1,2,3
print(a,b,c) # 1 2 3
print("number",a,b,c) # number 1 2 3

print(a,b,c,sep=',') #1,2,3
print(a,b,c, sep='') #123

print(a,b,c, sep='\n')
#1
#2
#3

print(a) # 1
print(b) # 2
print(c) # 3
print(a, end='') #print에 있는 기본적인 줄바꿈 없애기
print(b, end='')
print(c, end='')