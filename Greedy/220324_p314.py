# n개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값
# 오름차순 정렬
# target: 나 이거까진 만들 수 있는데 
# 너는 몇인데???? : coins[i]
# 나는 7인데 너는 9야...? 곤란한데..? 
import time
n = map(int, input().split())
coins = list(map(int, input().split()))

start_time = time.time() # 측정 시작

coins.sort()

target = 1

for i in coins:
    if(target < i):    
        break
    target += i
    print(target, i)
print(target)       
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
