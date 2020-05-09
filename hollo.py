n=int(input())
print(" "*(2*n),end="*")
print()
j=1
for i in range(n-1,-1,-1):
    print("  "*i,end="*")
    print(" "*(2*(2*j-1)+1),end="*")
    print()
    j+=1
j=n-1
for i in range(1,n):
    print("  "*i,end="*")
    print(" "*(2*(2*j-1)+1),end="*")
    print()
    j-=1

print(" "*(2*n),end="*")
    
    
