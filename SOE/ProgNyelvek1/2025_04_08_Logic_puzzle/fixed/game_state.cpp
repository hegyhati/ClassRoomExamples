#include "game_state.hpp"
#include <algorithm>

GameState::GameState() : boatleft(true) {
    std::fill(onleft.begin(), onleft.end(), true);
}

bool GameState::isOver() const {
    return std::none_of(onleft.begin(), onleft.end(), std::identity());
}

bool GameState::try_move(const Travelers& travelers) {
    if (!validBoat(travelers)) return false;
    move(travelers);
    if (validState()) return true;
    move(travelers);
    return false;
}

bool GameState::validState() const {
    return cannotHurt(father, {girl1, girl2}, mother) && cannotHurt(mother, {boy1, boy2}, father) &&
           cannotHurt(murderer, {father, mother, girl1,girl2,boy1,boy2}, police);
}

bool GameState::cannotHurt(People attacker, const std::initializer_list<People>& victims, People defender) const {
    return std::all_of(victims.begin(), victims.end(), [&attacker, &defender, this](People victim) { 
        return onleft[attacker] != onleft[victim] || onleft[attacker] == onleft[defender]; 
    });
}

bool GameState::hasAdult(const Travelers& travelers){
    return isAdult(travelers.first) || (travelers.second.has_value() && isAdult(*travelers.second));
}

bool GameState::isAdult(People person) {
    return (adults & (1 << person)) != 0;
}

bool GameState::validBoat(const Travelers& travelers) const{
    if (onleft[travelers.first] != boatleft) return false;
    if (travelers.second.has_value() && onleft[*travelers.second] != boatleft) return false;
    return hasAdult(travelers);
}

void GameState::move(const Travelers& travelers) {
    boatleft xor_eq true;
    onleft[travelers.first] xor_eq true;
    if (travelers.second.has_value()) onleft[*travelers.second] xor_eq true;    
}


std::ostream& operator << (std::ostream& s, const GameState& gs) {
    s << "Csonak: "<< (gs.boatleft ? "bal" : "jobb");
    s << "\nBal:";
    for(unsigned int i = 0; i < GameState::people_max; ++i) 
        if (gs.onleft[i]) s << " " << GameState::names[i];    
    s << "\nJobb:";
    for(unsigned int i = 0; i < GameState::people_max; ++i) 
        if (!gs.onleft[i]) s << " " << GameState::names[i];
    return s << "\n";
}

const std::array<std::string,GameState::people_max> GameState::names = {"Apa", "Anya", "Fiu1", "Fiu2", "Lany1", "Lany2", "Gyilkos", "Rendor"}; 

std::optional<GameState::People> GameState::getPersonByString(const std::string_view& name) {
    auto name_pos = find(GameState::names.begin(), GameState::names.end(), name);
    if (name_pos == GameState::names.end()) return std::nullopt;
    return static_cast<GameState::People>(name_pos - GameState::names.begin());
}
