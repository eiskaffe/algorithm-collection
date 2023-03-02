N = input()
n = int(N[:-1])
k = int(N[-1])
t = []
while n > 0:
    N = str(n - (k*3))
    if int(N) < 0: break
    t.append(N)
    if int(N) < 31: break
    n = int(N[:-1])
    k = int(N[-1])

print("IGEN" if len(t) > 0 and t[-1] == "0" else "NEM")
if len(t) > 0: print(" ".join(t))