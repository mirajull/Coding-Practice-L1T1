def row(x,y,z):
    if (x<=2*y-1):
        if (x>y):
            z-=1
        else:
            z+=1
        print(z,end=' ')
        return row(x+1,y,z)

n=int(input())
i=0
def triangle(m,n,i):
    if m<=n:
        print(' '*2*(n-m),end='')
        row(1,m,i)
        print()
        
        return triangle(m+1,n,i+1)
triangle(1,n,0)
