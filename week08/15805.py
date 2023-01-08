#윤호는 관광 가이드
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [0] * 200000
parent = [0] * 200000
visit = [False] * 200000

inp = list(map(int, input().split()))

for i in range (1, n + 1):
	arr[i] = inp[i - 1]

ans = 0
child = 0

for i in range (1, n + 1):
	if not visit[arr[i]] :
		ans += 1
		visit[arr[i]] = True
		child = arr[i]
	else :
		parent[child] = arr[i]
		child = arr[i]

parent[child] = -1

print(ans)
for i in range (ans) :
	print(parent[i], end = ' ')