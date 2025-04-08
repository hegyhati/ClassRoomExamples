#pragma once

#include <optional>
#include <ostream>
#include <array>
#include <string>



class GameState {
    
public:
    enum People {father=0, mother, boy1, boy2, girl1, girl2, murderer, police, people_max};    
    using Travelers = std::pair<People, std::optional<People>>; 
    const static std::array<std::string,people_max> names; // not nice here
    static std::optional<People> getPersonByString(const std::string_view& name);
    
private:
    static constexpr int adults = (1 << father) | (1 << mother) | (1 << police);  
    std::array<bool,people_max> onleft;
    bool boatleft;

public: 

    GameState();

    bool isOver() const;
    bool try_move(const Travelers& travelers);

private:
    bool validState() const;
    bool cannotHurt(People attacker, const std::initializer_list<People>& victims, People defender) const;
    static bool hasAdult(const Travelers& travelers);
    static bool isAdult(People person);
    bool validBoat(const Travelers& travelers) const;
    void move(const Travelers& travelers) ;

    friend std::ostream& operator << (std::ostream& s, const GameState& gs);
};


