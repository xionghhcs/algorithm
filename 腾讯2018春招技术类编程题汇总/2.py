n = int(input())

data = list(map(int, input().strip().split(' ')))

data = sorted(data, reverse=True)

sub_data = [v for idx, v in enumerate(data) if idx % 2 == 0]

nn = sum(sub_data)


print(2 * nn - sum(data))



