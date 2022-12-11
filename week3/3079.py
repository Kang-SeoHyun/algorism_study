import sys
input = sys.stdin.readline

N, M = map(int, input().split())
time = [int(input()) for _ in range(N)]

start = min(time)
end = max(time) * M
result = max(time) * M

while start <= end :
	mid = (start + end) // 2
	total = 0 #입국 할 수 있는 사람 수
	for i in range(N):
		total += mid // time[i]
	
