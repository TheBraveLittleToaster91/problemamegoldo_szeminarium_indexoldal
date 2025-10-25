# Reading Books
# https://cses.fi/problemset/task/1631/

import sys

def solve():
    # Gyors input olvasás
    def input_line():
        return sys.stdin.readline().strip()

    try:
        n = int(input_line())
    except:
        return

    try:
        if n == 0:
            print(0)
            return
        
        T = list(map(int, input_line().split()))
    except:
        return

    # 1. Összes olvasási idő (sum t_i)
    total_time_sum = sum(T)
    
    # 2. Leghosszabb könyv olvasási ideje (T_max)
    max_time = 0
    if T:
        max_time = max(T)
    
    # 3. Minimum teljes idő meghatározása
    # A minimális idő a nagyobb a két érték közül:
    # a) Az összes olvasási idő.
    # b) Kétszer a leghosszabb könyv ideje (a szűk keresztmetszet miatti késleltetés).
    
    # A képlet: max(sum(T), 2 * max(T))
    minimum_total_time = max(total_time_sum, 2 * max_time)
    
    print(minimum_total_time)

solve()