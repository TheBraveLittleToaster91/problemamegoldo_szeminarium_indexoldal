# Dinamikus programozás - Distinct Values Subsequences
# https://cses.fi/problemset/task/3421/

import sys

# Globális moduló érték
MOD = 10**9 + 7

def solve():
    # Gyors input olvasás
    def input_line():
        return sys.stdin.readline().strip()

    try:
        n = int(input_line())
        if n == 0:
            print(0)
            return
        A = list(map(int, input_line().split()))
    except:
        return

    # TotalCount: A jelenlegi indexig talált, különböző elemekből álló ÖSSZES részsorozat száma.
    total_count = 0 
    
    # dp_last: Szótár, ami az adott értékkel (kulcs) végződő, különböző elemekből álló 
    # részsorozatok számát tárolja (érték), az érték UTOLSÓ előfordulásánál.
    # dp_last[x] = DP állapot, ami x-ben végződik
    dp_last = {} 

    for x in A:
        # 1. Hány új részsorozatot képezünk az aktuális 'x' használatával?
        # Ez az összes korábbi részsorozat (total_count) + az egyelemű [x].
        # new_subsequences_ending_at_x adja az új DP[x] értéket.
        new_subsequences_ending_at_x = (total_count + 1) % MOD
        
        # 2. Korrekciós mennyiség: Mennyi volt az x-ben végződő sorozatok száma
        # a legutóbbi x előfordulásánál?
        # Ezek a sorozatok a total_count-ban voltak, és most le kell cserélni őket.
        old_count_ending_at_x = dp_last.get(x, 0)
        
        # 3. TotalCount frissítése
        # A változás a total_count-ban: 
        # (Új, x-ben végződő sorozatok) - (Régi, x-ben végződő sorozatok)
        change = (new_subsequences_ending_at_x - old_count_ending_at_x + MOD) % MOD
        
        # TotalCount_új = TotalCount_előző + változás
        total_count = (total_count + change) % MOD 
        
        # 4. DP[x] frissítése
        # A jelenlegi, x-ben végződő részsorozatok száma most már az új érték.
        dp_last[x] = new_subsequences_ending_at_x

    # A végeredmény a végén lévő total_count.
    print(total_count)

solve()