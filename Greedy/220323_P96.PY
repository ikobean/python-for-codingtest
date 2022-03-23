import time
# 가장 작은 수 모음에서 가장 큰 수 찾기
# 각 행 마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수 를 찾는 ㄱ넛
m, n = map(int, input().split())

start_time = time.time() # 측정 시작



result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value, result)

print(result)

end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력