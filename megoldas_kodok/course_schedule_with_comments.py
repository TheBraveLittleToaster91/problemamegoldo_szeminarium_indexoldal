# Gráfos - Course Schedule (Kahn-algoritmus)
# https://cses.fi/problemset/task/1679/

import sys
from collections import deque

def solve():
    # Input beolvasása (n, m)
    data = sys.stdin.readline().split()
    if not data:
        print("IMPOSSIBLE")
        return
    
    n = int(data[0])  # Kurzusok száma
    m = int(data[1])  # Követelmények száma

    # Gráf reprezentálása szomszédsági listával (adj[a] tartalmazza a-nak az utódait, azaz azokat a kurzusokat, 
    # amelyekhez a-nak előfeltételként kell teljesülnie)
    adj = [[] for _ in range(n + 1)]
    
    # Bejövő élek számának tárolása (hány előfeltétele van egy kurzusnak)
    indegree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        # a-nak b előtt kell teljesülnie
        adj[a].append(b)
        # b-nek eggyel több előfeltétele van (az 'a' kurzus)
        indegree[b] += 1
    
    # --- Kahn-algoritmus ---
    
    # 1. Inicializáljuk a sort a 0 bejövő éllel rendelkező csúcsokkal
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    # 2. Topológiai sorrend tárolása
    result = []

    # 3. Feldolgozás
    while queue:
        u = queue.popleft()
        result.append(u)

        # Vizsgáljuk meg a kurzus összes utódját (v)
        for v in adj[u]:
            # Csökkentjük az utód bejövő éleinek számát, 
            # mintha épp most teljesítettük volna az 'u' kurzust
            indegree[v] -= 1

            # Ha az utódnak már nincs több előfeltétele, mehet a sorba
            if indegree[v] == 0:
                queue.append(v)
    
    # 4. Ciklus detektálása
    if len(result) == n:
        # Minden kurzust feldolgoztunk, van megoldás
        print(*(result))
    else:
        # A result lista mérete kisebb, mint n. Ez azt jelenti, hogy 
        # maradtak olyan csúcsok, amelyeknek a bejövő éle nem érte el a 0-t.
        # Ez csak akkor lehetséges, ha van egy ciklus a gráfban, ami lehetetlenné teszi a teljesítést.
        print("IMPOSSIBLE")

solve()