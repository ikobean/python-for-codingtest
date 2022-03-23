import time
n, k = map(int, input().split())

start_time = time.time() # 측정 시작
result = 0

while (n != 1):
    # k로 나누어지는 수가 될 때 까지 1씩 빼기 대신 수행
    # n 을 k로 나눈 몫에 k를 곱하면 n과 가장 가까운 수 중에 k의 배수가 나옴
    target = (n // k) * k

    # n - 배수 => 빼기 해야되는 count
    result += (n - target)
    n = target

    result += 1
    n //= k
    print(n)

# 마지막으로 남은 수에 대하여 1씩 빼기 
# 이해가 안된다... 왜...???? 220323
# result += (n-1)
print(result)

end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
