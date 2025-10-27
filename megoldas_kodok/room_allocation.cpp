#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    if (!(std::cin >> n) || n == 0) {
        std::cout << "0\n";
        return 0;
    }

    std::vector<std::tuple<int, int, int>> customers;
    customers.reserve(n);
    for (int i = 0; i < n; ++i) {
        int a, b;
        if (std::cin >> a >> b) {
            customers.emplace_back(a, b, i);
        }
    }

    std::sort(customers.begin(), customers.end(),
              [](const auto& x, const auto& y) {
                  return std::get<0>(x) < std::get<0>(y);
              });

    std::vector<int> room_allocations(n, 0);

    std::priority_queue<std::pair<int, int>,
                        std::vector<std::pair<int, int>>,
                        std::greater<>> booked_rooms;

    std::priority_queue<int, std::vector<int>, std::greater<>> available_room_ids;
    for (int i = 1; i <= n; ++i) {
        available_room_ids.push(i);
    }

    int max_rooms_needed = 0;

    for (auto& [arrival, departure, original_index] : customers) {
        if (!booked_rooms.empty() && booked_rooms.top().first < arrival) {
            auto [old_departure, room_id] = booked_rooms.top();
            booked_rooms.pop();

            room_allocations[original_index] = room_id;
            booked_rooms.emplace(departure, room_id);
        } else {
            int room_id = available_room_ids.top();
            available_room_ids.pop();
            max_rooms_needed = std::max(max_rooms_needed, room_id);

            room_allocations[original_index] = room_id;
            booked_rooms.emplace(departure, room_id);
        }
    }

    std::cout << max_rooms_needed << "\n";
    for (int i = 0; i < n; ++i) {
        std::cout << room_allocations[i] << (i + 1 == n ? '\n' : ' ');
    }

    return 0;
}