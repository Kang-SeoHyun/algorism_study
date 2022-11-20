n = int(input())

a = list(map(int, input().split()))
answer = [0] * n
result = -1000

for i in range(0, n):
	answer[i] = max(answer[i-1] + a[i], a[i])
	result = max(answer[i], result)

print(result)