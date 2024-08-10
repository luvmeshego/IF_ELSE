height = int(input())
long = int(input())
piece = int(input())
if (piece // long) or (piece // height) and  long * height:
    print('YES')
else:
    print('NO')