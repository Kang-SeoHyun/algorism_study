a = list(input())
b = list(input())
answer = ''

def add(i, j):
	i = int(i)
	j = int(j)
	return str((i + j) % 10)

for i in range(8):
	answer += a[i] + b[i]

while len(answer) != 2:
	temp = []
	for i in range(len(answer) - 1):
		temp.append(add(answer[i], answer[i+1]))
	answer = ''.join(temp)

print(answer)