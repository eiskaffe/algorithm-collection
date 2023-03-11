N, M, K = input().split()
N = int(N)

kereskedok = []
aruk_eladasa = {} # Mivel M<=100, ezért dictionary alkalmazható
aru_lista = {} # Key: aru; values: eladott mennyiség, ar, kereskedőszám
total_szum = 0
for id in range(N): # O(N)
    kereskedo_be = list(map(int, input().split()))
    kereskedo = {}
    szum = 0
    for i in range(0, kereskedo_be.pop(0)*3, 3): # Áruk elemzése
        aruid = kereskedo_be[i]
        aruar = kereskedo_be[i+1]
        arueladas = kereskedo_be[i+2]
        
        kereskedo[aruid] = (aruar, arueladas)
        szum += aruar*arueladas
        aruk_eladasa[aruid] = aruk_eladasa.get(aruid, 0) + arueladas
        
        if aru_lista.get(aruid, [0,0])[1] <= aruar:
            if aru_lista.get(aruid, [0,0])[1] < aruar and \
                aru_lista.get(aruid, [0])[0] < arueladas:
                    aru_lista[aruid] = (aruar, arueladas, id+1)
            elif aru_lista.get(aruid, -1) != -1:
                aru_lista.pop(aruid)
    
    kereskedo["szum"] = szum
    total_szum += szum
    kereskedok.append(kereskedo)

# A O(2N)
atlag = total_szum / N
# print(kereskedok, N, atlag)
atlagfeletti = [(kereskedo["szum"], i+1) 
                for i, kereskedo in enumerate(kereskedok)
                if kereskedo["szum"] >= atlag]
print(len(atlagfeletti), end=" ")
for kereskedo in sorted(atlagfeletti, reverse=True):
    print(kereskedo[1], end=" ")
print()

# B O(K)
# print(aruk_eladasa)
print(max(aruk_eladasa.items(), key=lambda x:x[1])[0])

# C
# print(aru_lista)
smallest_key = min(aru_lista.keys())
print(aru_lista[smallest_key][2])