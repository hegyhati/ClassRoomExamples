#include <iostream>
#include <string>
#include <optional>
#include <tuple>
#include <algorithm>
#include <string_view>

using namespace std;

#include "game_state.hpp"



std::string_view trim(const std::string_view& str) {
    auto start = str.find_first_not_of(" ");
    if (start == std::string_view::npos) return "";
    auto end = str.find_last_not_of(" ");
    return str.substr(start, end - start + 1);
}


pair<optional<GameState::People>,optional<GameState::People>> fetch_people_from_string(const string_view& s) {
    const auto pos = s.find(",");
    if (pos == string_view::npos) return { GameState::getPersonByString(trim(s)), nullopt };
    else return {
        GameState::getPersonByString(trim(s.substr(0,pos))),
        GameState::getPersonByString(trim(s.substr(pos+1)))
    };
}

int main() {

    GameState game;
    string travellers;
    while (!game.isOver()) {
        cout << game;
        cout << "\nKik menjenek a tuloldalra:  ";
        while (true) {
            getline(cin, travellers);
            auto [p1,p2] = fetch_people_from_string(travellers);
            if (!p1.has_value()) {
                cout << "Nem jo, egy, vagy vesszovel elvalasztva ket letezo utas: ";
            } else if (!game.try_move({*p1,p2})) {
                cout << "Nem megengedett, probalkozz ujra: ";
            } else break;
        }
    }
    cout << "Wooohoooo!\n\n";
}