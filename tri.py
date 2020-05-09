n=int(input())
m=1
def tri(n,m):
    for i  in range(n-1,-1,-1):
        print(' '*i,end='')
        for j in range(1,m+1,2):
            print(j,end='')
        for j in range(m-2,0,-2):
            print(j,end='')
        
        m+=2
        print()
def tr(n):
    tri(n,1)
tr(n)
