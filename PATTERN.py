def triangle(N):
    for i in range(N,0,-1):
        for j in range(i):
            print("*",end ="")
        print("")


def hollow_box(N):
    for i in range(N):
        for j in range(N):
            if(i==0 or i ==N-1 or j==0 or j==N-1):
                print("*",end='')
            else:
                print("",end=' ')
        print()

hollow_box(4)


