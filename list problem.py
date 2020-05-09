m=int(input())
n=int(input())
l1=[]
l2=[]
for i in range(m):
    l1.append(int(input()))
for i in range(n):
    l2.append(int(input()))

print(l1,l2)

def find(a,b):
    l=len(b)
    for i in range(l):
        if a==b[i]:
            return 1

ans=[]
for i in range(m):
    for j in range(n):
        if l1[i]==l2[j] and find(l2[j],ans)!=1:
            ans.append(l2[j])

ans2=[]
for i in range(m):
    if find(l1[i],ans2)!=1:
        ans2.append(l1[i])


for i in range(n):
    if find(l2[i],ans2)!=1:
        ans2.append(l2[i])

print(ans,ans2)
