height = int(input())
length = int(input())
piece = int(input())
if (piece % length == 0 or piece % height == 0) and piece < length * height:
    print('YES')
else:
    print('NO')