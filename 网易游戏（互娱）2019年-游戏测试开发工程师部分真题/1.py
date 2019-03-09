w = list(map(int, input().strip().split(' ')))

w_dict = {idx:v for idx, v in enumerate(w)}

s = input().strip()

row = 1
cur_row_len = 0
char_num = 0
for c in s:
    if cur_row_len + w_dict[ord(c) - ord('a')] <= 100:
        cur_row_len += w_dict[ord(c) - ord('a')]
        char_num += 1
    else:
        row += 1
        char_num = 1
        cur_row_len = w_dict[ord(c) - ord('a')]

print('{} {}'.format(row, cur_row_len))