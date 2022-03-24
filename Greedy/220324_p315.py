import time
m, n = map(int, input().split())
weight = list(map(int, input().split()))
start_time = time.time() # 측정 시작
'''
n = 공의 개수
m = ~까지 공의 무게
'''
result = 0

for i in range(m-1):
    for j in range(i+1, m):
        if(weight[i] != weight[j]):
            result += 1


print(result)

end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
