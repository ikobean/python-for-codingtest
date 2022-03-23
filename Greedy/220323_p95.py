n, m, k = map(int, input().split())

data = list(map(int, input().split()))


data.sort()

big = data[-1]
small = data[-2]
count = int( m / k+1 + m % k + 1)

answer = big * count + small * (m - count)

print(answer)
