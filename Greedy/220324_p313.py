import time

data = input()
start_time = time.time() # 측정 시작


#문자열이 1, 0몇 덩어리인지 구한다
#작은 덩어리의 수를 반환한다.

## 처음 연속하는 두개의 숫자로 모든 숫자를 바꾼다?

##연속된 숫자를 잡고 모두 뒤집는다.
#0001100
#숫자 한개만 세면 되지 않나?
#

count_one = 0
count_zero = 0
before = int(data[0])
for i in range(1, len(data)):
    if(before == int(data[i])):
        continue
    else:
        
        if(int(data[i]) == 0):
            before = 0
            count_zero += 1
        else:
            before = 1
            count_one += 1

answer = min(count_zero, count_one)
print(answer)

end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력