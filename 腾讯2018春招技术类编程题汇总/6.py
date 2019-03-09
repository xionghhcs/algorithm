m, n = list(map(int, input().strip().split(' ')))
data = []
for _ in range(m):
    row = list(input().strip())
    data.append(row)

cnt = 0
for i in range(m):
    for j in range(n):
        if data[i][j] == 'G':
            cnt += 2
            row = i + 1
            col = j + 1
            while row < m and col < n:
                if data[row][col] == 'Y':
                    data[row][col] = 'X'
                    row += 1
                    col += 1
                elif data[row][col] == 'G':
                    data[row][col] = 'B'
                    row += 1
                    col += 1
                else:
                    break
            row = i + 1
            col = j - 1
            while row < m and col >=0:
                if data[row][col] == 'B':
                    data[row][col] = 'X'
                    row += 1
                    col -= 1
                elif data[row][col] == 'G':
                    data[row][col] = 'Y'
                    row += 1
                    col -= 1
                else:
                    break
        elif data[i][j] == 'Y':
            cnt += 1
            row = i + 1
            col = j + 1
            while row < m and col < n:
                if data[row][col] == 'Y':
                    data[row][col] = 'X'
                    row += 1
                    col += 1
                elif data[row][col] == 'G':
                    data[row][col] = 'B'
                    row += 1
                    col += 1
                else:
                    break
        elif data[i][j] == 'B':
            cnt += 1
            row = i + 1
            col = j - 1
            while row < m and col >=0:
                if data[row][col] == 'B':
                    data[row][col] = 'X'
                    row += 1
                    col -= 1
                elif data[row][col] == 'G':
                    data[row][col] = 'Y'
                    row += 1
                    col -= 1
                else:
                    break

print(cnt)

