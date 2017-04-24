
def triangles():
    L = [1]
    while True: 
        yield L
        L = [1] + [L[i]+L[i+1] for i in range(0, len(L)-1)] + [1]

n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break
