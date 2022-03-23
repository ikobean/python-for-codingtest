import time
# 모험가 공포도
# 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여
# 최대 몇개 모험가 그룹?
# 2 3 1 2 2 => 2
n = map(int, input().split())
fear = list(map(int, input().split()))

start_time = time.time() # 측정 시작

fear.sort()

count = 0
result = 0

for i in fear:
    count += 1
    if(count >= i) : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
        result += 1
        count = 0

print(result)

end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력


