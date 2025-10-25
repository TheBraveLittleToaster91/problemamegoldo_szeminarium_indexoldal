# Room Allocation
# https://cses.fi/problemset/task/1164/

import heapq
import sys

def solve():
    # Gyors input olvasás
    def input_line():
        return sys.stdin.readline().strip()

    try:
        n = int(input_line())
        if n == 0:
            print("0\n")
            return
    except:
        return

    # Az ügyfél adatok beolvasása (a, b, eredeti_index)
    customers = []
    for i in range(n):
        try:
            a, b = map(int, input_line().split())
            customers.append((a, b, i))
        except:
            pass

    # 1. Rendezés: Érkezési nap (a) alapján növekvő sorrendben
    # A rendezés csak az első két elemen történik (a, b).
    customers.sort(key=lambda x: x[0])

    # Room ID-k tárolása az eredeti index alapján
    room_allocations = [0] * n
    
    # Min-heap a szobák szabaddá válási napjainak tárolására
    # Elemek: (távozás_napja, szoba_ID)
    free_rooms = [] 
    
    # Heap a szabad szoba ID-k tárolására
    # Mivel szeretnénk a legkisebb, már felszabadult szobát újrahasználni,
    # egy külön min-heap tárolja az ID-kat.
    available_room_ids = []
    for i in range(1, n + 1): # A szoba ID-k 1-től n-ig
        heapq.heappush(available_room_ids, i)

    # A szükséges szobák számát a felhasznált ID-k száma adja
    max_rooms_needed = 0

    # 3. Szobakiosztás
    for arrival, departure, original_index in customers:
        
        # Van-e már felszabadult szoba a legkorábban felszabadulók közül?
        # Feltétel: free_rooms teteje (távozás napja) < arrival
        if free_rooms and free_rooms[0][0] < arrival:
            
            # 1. Újrahasznosítás: Kiveszünk egy felszabadult szobát
            # A szoba legkorábbi távozási napja (old_departure) és ID-ja
            old_departure, room_id = heapq.heappop(free_rooms)
            
            # 2. Hozzárendelés: Az ügyfél megkapja a felszabadult szobát
            room_allocations[original_index] = room_id
            
            # 3. Frissítés: A szoba új szabaddá válási napját betesszük a heap-be
            heapq.heappush(free_rooms, (departure, room_id))

        else:
            # 1. Új szoba kell: Növeljük a felhasznált szobák számát (max_rooms_needed)
            # A szoba ID-t a rendelkezésre álló ID-k közül vesszük
            room_id = heapq.heappop(available_room_ids)
            max_rooms_needed = max(max_rooms_needed, room_id)
            
            # 2. Hozzárendelés: Az ügyfél megkapja az új szobát
            room_allocations[original_index] = room_id
            
            # 3. Frissítés: Az új szoba távozási napját betesszük a heap-be
            heapq.heappush(free_rooms, (departure, room_id))


    # --- Output ---
    
    # 1. Minimum szükséges szobák száma
    print(max_rooms_needed)
    
    # 2. Szobakiosztás az eredeti bemeneti sorrendben
    print(*(room_allocations))

solve()