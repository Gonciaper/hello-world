#十行十列变色
i = 0

while i < 100:
    if i % 2 == 0:
        print('✩', end='')
    else :
        print('✭', end='')
    if i % 10 ==9:
        print('\n', end='')
    i += 1
