for i in range(0,6):

    for j in range(1, 6-i):
        print(' ', end=' ')

    
    for j in range(1,i+1):
        print(j, end=' ')

    for j in range(1,i):
        print(j,end=' ')

    print()