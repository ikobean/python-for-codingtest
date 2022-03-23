import time
import sys
'''
내가 놓친 부분
첫번재 인덱스로 초기화 한 후 비교하기.

'''

data = input()

start_time = time.time() # 측정 시작

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if(num <= 1 or result <= 0):
        result += num
    else: result *= num

print(result)
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력


''' 내 풀이
#str = sys.stdin.readline().rstrip()
data = input()
start_time = time.time() # 측정 시작

result = 0
for i in str:
    num = int(i)
    print(num)
    if(num == 0 or num == 1 or result == 0):
        result += num
    else: result *= num

print(result)
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
'''