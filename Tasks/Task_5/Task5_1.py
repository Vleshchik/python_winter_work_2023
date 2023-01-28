n = int(input())
pas_tri = [[1]]
print(pas_tri[0])
for i in range(1,n+1):
    pas_tri.append([1])
    for j in range(len(pas_tri[i-1])-1):
        pas_tri[i].append(pas_tri[i-1][j]+pas_tri[i-1][j+1])
    pas_tri[i].append(1)
    print(pas_tri[i])