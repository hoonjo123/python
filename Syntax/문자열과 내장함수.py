#1. upper
msg = "It is Time"

print(msg.upper()) #IT IS TIME
print(msg)

#2. lower
print(msg.lower()) #it is time

#3. 
tmp = msg.upper()
print(tmp)
print(tmp.find('T')) #index number 1

#4.
print(tmp.count('T')) #2

#5.
print(msg[:2]) #It 0~1까지
print(msg[3:5]) #is

#.
print(len(msg)) #10
for i in range(len(msg)):
  print(msg[i],end=' ') #I t   i s   T i m e
print()

for j in msg:
  print(j, end='') #It is Time
print()

#대분자만 출력하기
for j in msg:
  if j.isupper():
    print(j, end=' ')
print()


#알파벳만 출력하기
for x in msg:
  if x.isalpha():
    print(x,end="") #ItisTime
print() 

#아스키넘버 출력하기
temp = "AZ"
for x in temp:
  print(ord(x)) #65 90
print()

#아스키넘버 문자로 출력하기
tmp = 65
print(chr(tmp)) #A





